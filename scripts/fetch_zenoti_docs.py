#!/usr/bin/env python3
"""
Zenoti API Documentation Scraper

Scrapes documentation from docs.zenoti.com using Playwright for
browser automation (required due to ReadMe.io's JavaScript rendering).

Features:
- Extracts all endpoints from sidebar navigation
- Focuses on Python code examples
- Handles tabbed content interfaces
- Fallback extraction when specific selectors fail
"""

import json
import hashlib
import logging
import re
import time
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional, Set
from urllib.parse import urljoin, urlparse

from playwright.sync_api import sync_playwright, Page, Browser, TimeoutError as PlaywrightTimeout
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Configuration
BASE_URL = "https://docs.zenoti.com"
MANIFEST_FILE = "docs_manifest.json"
RATE_LIMIT_DELAY = 2.0  # seconds between requests
DEFAULT_TIMEOUT = 60000  # 60 seconds
NAV_TIMEOUT = 30000  # 30 seconds for navigation


class ZenotiDocsScraper:
    """Scraper for Zenoti API documentation."""

    def __init__(self, output_dir: Path, headless: bool = True):
        self.output_dir = output_dir
        self.headless = headless
        self.manifest = self._load_manifest()
        self.browser: Optional[Browser] = None
        self.page: Optional[Page] = None
        self.scraped_urls: Set[str] = set()

    def _load_manifest(self) -> dict:
        """Load existing manifest or create new one."""
        manifest_path = self.output_dir / MANIFEST_FILE
        if manifest_path.exists():
            try:
                return json.loads(manifest_path.read_text())
            except Exception as e:
                logger.warning(f"Failed to load manifest: {e}")
        return {"files": {}, "last_updated": None}

    def _save_manifest(self, manifest: dict) -> None:
        """Save manifest to file."""
        manifest_path = self.output_dir / MANIFEST_FILE
        manifest["last_updated"] = datetime.now().isoformat()
        manifest["base_url"] = "https://raw.githubusercontent.com/tacit-code/zenoti-docs/main/docs/"
        manifest["source"] = "docs.zenoti.com"
        manifest_path.write_text(json.dumps(manifest, indent=2))

    def _content_hash(self, content: str) -> str:
        """Generate SHA256 hash of content."""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    def _wait_for_page_load(self, timeout: int = DEFAULT_TIMEOUT) -> bool:
        """Wait for page to fully load."""
        try:
            self.page.wait_for_load_state("networkidle", timeout=timeout)
            return True
        except PlaywrightTimeout:
            logger.warning("Page load timeout, continuing with available content")
            return False

    def _safe_click(self, selector: str, timeout: int = 5000) -> bool:
        """Safely click an element, returning False if not found."""
        try:
            element = self.page.locator(selector).first
            if element.is_visible(timeout=timeout):
                element.click()
                time.sleep(0.5)
                return True
        except Exception:
            pass
        return False

    def _extract_visible_text(self) -> str:
        """Extract all visible text content from the page."""
        try:
            # Get the main content area
            content = self.page.locator("main, article, [class*='content']").first
            if content:
                return content.inner_text()
        except Exception:
            pass
        return self.page.inner_text("body")

    def _extract_code_blocks(self) -> List[Dict[str, str]]:
        """Extract all code blocks from the page."""
        code_blocks = []
        try:
            # Look for pre/code elements
            code_elements = self.page.locator("pre, code, [class*='code'], [class*='CodeBlock']").all()
            for elem in code_elements:
                try:
                    text = elem.inner_text()
                    if text and len(text.strip()) > 10:
                        # Try to determine language
                        classes = elem.get_attribute("class") or ""
                        lang = "python" if "python" in classes.lower() else ""
                        code_blocks.append({"code": text.strip(), "language": lang})
                except Exception:
                    continue
        except Exception as e:
            logger.debug(f"Error extracting code blocks: {e}")
        return code_blocks

    def _click_python_tab(self) -> bool:
        """Try to click Python tab in code examples."""
        python_selectors = [
            "button:has-text('Python')",
            "[data-language='python']",
            "tab:has-text('Python')",
            "[class*='tab']:has-text('Python')",
            "li:has-text('Python')",
        ]
        for selector in python_selectors:
            if self._safe_click(selector):
                logger.debug("Clicked Python tab")
                return True
        return False

    def _click_all_tabs_and_extract(self) -> Dict[str, str]:
        """Click through tabs and extract content from each."""
        tab_content = {}

        # Common tab selectors
        tab_selectors = [
            "[role='tab']",
            "[class*='tab']",
            "button[class*='Tab']",
        ]

        for tab_selector in tab_selectors:
            try:
                tabs = self.page.locator(tab_selector).all()
                for tab in tabs:
                    try:
                        tab_name = tab.inner_text().strip()
                        if tab_name and tab_name not in ['Try It!', 'Try it!', 'Response', 'Responses']:
                            tab.click()
                            time.sleep(0.3)
                            # Get code content after clicking
                            code_blocks = self._extract_code_blocks()
                            if code_blocks:
                                tab_content[tab_name] = code_blocks[0]["code"]
                    except Exception:
                        continue
            except Exception:
                continue

        return tab_content

    def _slugify(self, text: str) -> str:
        """Convert text to URL-safe slug."""
        text = text.lower()
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', '-', text)
        return text.strip('-')

    def _html_to_markdown(self, soup: BeautifulSoup) -> str:
        """Convert HTML content to markdown."""
        md_parts = []

        # Process headings
        for i in range(1, 7):
            for h in soup.find_all(f'h{i}'):
                md_parts.append(f"{'#' * i} {h.get_text().strip()}\n\n")

        # Process paragraphs
        for p in soup.find_all('p'):
            text = p.get_text().strip()
            if text:
                md_parts.append(f"{text}\n\n")

        # Process lists
        for ul in soup.find_all(['ul', 'ol']):
            for li in ul.find_all('li', recursive=False):
                md_parts.append(f"- {li.get_text().strip()}\n")
            md_parts.append("\n")

        # Process tables
        for table in soup.find_all('table'):
            rows = table.find_all('tr')
            if rows:
                # Header
                headers = rows[0].find_all(['th', 'td'])
                if headers:
                    md_parts.append("| " + " | ".join(h.get_text().strip() for h in headers) + " |\n")
                    md_parts.append("|" + "|".join("---" for _ in headers) + "|\n")
                # Body
                for row in rows[1:]:
                    cells = row.find_all(['td', 'th'])
                    if cells:
                        md_parts.append("| " + " | ".join(c.get_text().strip() for c in cells) + " |\n")
                md_parts.append("\n")

        # Process code blocks
        for pre in soup.find_all('pre'):
            code = pre.get_text().strip()
            if code:
                lang = ""
                code_elem = pre.find('code')
                if code_elem:
                    classes = code_elem.get('class', [])
                    for cls in classes:
                        if 'python' in cls.lower():
                            lang = 'python'
                            break
                        elif 'bash' in cls.lower() or 'shell' in cls.lower():
                            lang = 'bash'
                            break
                        elif 'json' in cls.lower():
                            lang = 'json'
                            break
                md_parts.append(f"```{lang}\n{code}\n```\n\n")

        return "".join(md_parts)

    # ========== RECIPE SCRAPING ==========

    def scrape_recipes_page(self) -> List[Tuple[str, str]]:
        """Scrape all recipes from the recipes page."""
        logger.info("Scraping recipes page...")
        results = []

        url = f"{BASE_URL}/recipes"
        self.page.goto(url, timeout=NAV_TIMEOUT)
        self._wait_for_page_load()
        time.sleep(RATE_LIMIT_DELAY)

        # Find all recipe cards/links
        recipe_links = []
        try:
            # Look for recipe cards with "Open Recipe" buttons or links
            cards = self.page.locator("[class*='recipe'], [class*='Recipe'], article, [class*='card']").all()
            for card in cards:
                try:
                    # Get recipe name from heading or title
                    title_elem = card.locator("h1, h2, h3, h4, [class*='title'], [class*='Title']").first
                    if title_elem.is_visible(timeout=1000):
                        title = title_elem.inner_text().strip()
                        if title and len(title) > 3:
                            recipe_links.append(title)
                except Exception:
                    continue
        except Exception as e:
            logger.warning(f"Error finding recipe cards: {e}")

        # Scrape each recipe
        for recipe_title in recipe_links:
            try:
                filename, content = self.scrape_single_recipe(recipe_title)
                if content:
                    results.append((filename, content))
            except Exception as e:
                logger.error(f"Failed to scrape recipe '{recipe_title}': {e}")

        # Fallback: extract page content if no individual recipes found
        if not results:
            logger.info("Using fallback extraction for recipes page")
            content = self._extract_page_as_markdown(url, "Recipes")
            if content:
                results.append(("recipes-overview.md", content))

        return results

    def scrape_single_recipe(self, recipe_title: str) -> Tuple[str, str]:
        """Scrape a single recipe by clicking on it."""
        logger.info(f"Scraping recipe: {recipe_title}")

        # Navigate to recipes page
        self.page.goto(f"{BASE_URL}/recipes", timeout=NAV_TIMEOUT)
        self._wait_for_page_load()
        time.sleep(1)

        # Find and click the recipe
        try:
            # Try clicking "Open Recipe" button near the title
            recipe_card = self.page.locator(f"text='{recipe_title}'").first
            if recipe_card:
                # Look for nearby button
                open_btn = self.page.locator(f":has-text('{recipe_title}') >> button:has-text('Open')").first
                if open_btn.is_visible(timeout=3000):
                    open_btn.click()
                else:
                    recipe_card.click()

                time.sleep(2)
                self._wait_for_page_load()
        except Exception as e:
            logger.warning(f"Could not click recipe '{recipe_title}': {e}")
            return "", ""

        # Click Python tab if available
        self._click_python_tab()
        time.sleep(0.5)

        # Extract content
        markdown = self._extract_recipe_content(recipe_title)
        filename = f"{self._slugify(recipe_title)}.md"

        # Try to close dialog if open
        self._safe_click("button:has-text('Close')")

        return filename, markdown

    def _extract_recipe_content(self, title: str) -> str:
        """Extract recipe content including all steps and Python code."""
        md = f"# {title}\n\n"
        md += f"**Source:** {BASE_URL}/recipes\n\n"
        md += "---\n\n"

        # Try to get description
        try:
            desc = self.page.locator("[class*='description'], [class*='Description'], p").first
            if desc.is_visible(timeout=2000):
                md += f"> {desc.inner_text().strip()}\n\n"
        except Exception:
            pass

        # Extract steps if visible
        steps = []
        try:
            step_elements = self.page.locator("[class*='step'], [class*='Step'], li").all()
            for i, step in enumerate(step_elements):
                try:
                    step_text = step.inner_text().strip()
                    if step_text and len(step_text) > 5:
                        steps.append({"number": i + 1, "content": step_text})
                except Exception:
                    continue
        except Exception:
            pass

        if steps:
            md += "## Steps\n\n"
            for step in steps:
                md += f"### Step {step['number']}\n\n"
                md += f"{step['content']}\n\n"

        # Extract Python code
        self._click_python_tab()
        time.sleep(0.5)

        code_blocks = self._extract_code_blocks()
        python_code = None
        for block in code_blocks:
            if 'import' in block['code'] or 'def ' in block['code'] or 'requests' in block['code']:
                python_code = block['code']
                break

        if not python_code and code_blocks:
            python_code = code_blocks[0]['code']

        if python_code:
            md += "## Python Implementation\n\n"
            md += f"```python\n{python_code}\n```\n\n"

        # Fallback: get all visible text if nothing else worked
        if len(md) < 200:
            visible_text = self._extract_visible_text()
            if visible_text:
                md += "## Content\n\n"
                md += visible_text[:5000]  # Limit length

        return md

    # ========== GUIDE SCRAPING ==========

    def scrape_guides(self) -> List[Tuple[str, str]]:
        """Scrape all guide pages."""
        logger.info("Scraping guides...")
        results = []

        # Get guide links from sidebar
        guide_urls = self._get_sidebar_links("/docs")

        if not guide_urls:
            # Fallback to predefined list
            guide_urls = [
                "/docs/overview",
                "/docs/create-the-backend-app-and-generate-a-new-api-key",
                "/docs/authentication",
                "/docs/zenoti-api-groups-1",
                "/docs/pagination",
                "/docs/response-and-error-codes",
                "/docs/api-rate-limits-1",
                "/docs/service-booking-apis",
                "/docs/product-sale-apis",
                "/docs/membership-sale-apis",
                "/docs/gift-card-sale-apis",
                "/docs/opportunity-apis"
            ]

        for url_path in guide_urls:
            if url_path in self.scraped_urls:
                continue
            self.scraped_urls.add(url_path)

            try:
                full_url = f"{BASE_URL}{url_path}" if url_path.startswith("/") else url_path
                slug = url_path.split("/")[-1] or "overview"

                content = self._extract_page_as_markdown(full_url, slug)
                if content:
                    filename = f"{self._slugify(slug)}.md"
                    results.append((filename, content))
                    logger.info(f"Scraped guide: {filename}")
            except Exception as e:
                logger.error(f"Failed to scrape guide {url_path}: {e}")

        return results

    # ========== REFERENCE SCRAPING ==========

    def scrape_reference(self) -> List[Tuple[str, str]]:
        """Scrape all API reference pages from sidebar navigation."""
        logger.info("Scraping API reference...")
        results = []

        # Get all reference links from sidebar
        ref_urls = self._get_sidebar_links("/reference")

        logger.info(f"Found {len(ref_urls)} reference endpoints")

        for url_path in ref_urls:
            if url_path in self.scraped_urls:
                continue
            self.scraped_urls.add(url_path)

            try:
                full_url = f"{BASE_URL}{url_path}" if url_path.startswith("/") else url_path
                slug = url_path.split("/")[-1]

                content = self._scrape_reference_endpoint(full_url, slug)
                if content:
                    filename = f"{self._slugify(slug)}.md"
                    results.append((filename, content))
                    logger.info(f"Scraped reference: {filename}")
            except Exception as e:
                logger.error(f"Failed to scrape reference {url_path}: {e}")

        return results

    def _get_sidebar_links(self, section_path: str) -> List[str]:
        """Extract all links from the sidebar navigation."""
        links = []

        try:
            # Navigate to section
            self.page.goto(f"{BASE_URL}{section_path}", timeout=NAV_TIMEOUT)
            self._wait_for_page_load()
            time.sleep(RATE_LIMIT_DELAY)

            # Find sidebar navigation
            sidebar_selectors = [
                "nav a[href*='/reference/']",
                "nav a[href*='/docs/']",
                "[class*='sidebar'] a",
                "[class*='Sidebar'] a",
                "[class*='nav'] a",
                "[class*='menu'] a",
            ]

            for selector in sidebar_selectors:
                try:
                    link_elements = self.page.locator(selector).all()
                    for link in link_elements:
                        try:
                            href = link.get_attribute("href")
                            if href and section_path.split("/")[1] in href:
                                # Normalize URL
                                if href.startswith("/"):
                                    links.append(href)
                                elif href.startswith(BASE_URL):
                                    links.append(href.replace(BASE_URL, ""))
                        except Exception:
                            continue
                except Exception:
                    continue

            # Remove duplicates while preserving order
            seen = set()
            unique_links = []
            for link in links:
                if link not in seen:
                    seen.add(link)
                    unique_links.append(link)
            links = unique_links

        except Exception as e:
            logger.warning(f"Error getting sidebar links for {section_path}: {e}")

        logger.info(f"Found {len(links)} links in sidebar for {section_path}")
        return links

    def _scrape_reference_endpoint(self, url: str, slug: str) -> str:
        """Scrape a single API reference endpoint."""
        logger.info(f"Scraping reference endpoint: {slug}")

        self.page.goto(url, timeout=NAV_TIMEOUT)
        self._wait_for_page_load()
        time.sleep(RATE_LIMIT_DELAY)

        # Click Python tab for code examples
        self._click_python_tab()
        time.sleep(0.5)

        # Extract content
        soup = BeautifulSoup(self.page.content(), 'html.parser')

        # Get title
        title = slug.replace("-", " ").title()
        title_elem = soup.find(['h1', 'h2'])
        if title_elem:
            title = title_elem.get_text().strip()

        md = f"# {title}\n\n"
        md += f"**Source:** {url}\n\n"

        # Try to extract HTTP method and endpoint URL
        method = ""
        endpoint = ""

        # Look for method badge (GET, POST, etc.)
        method_patterns = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
        page_text = self.page.inner_text("body")
        for m in method_patterns:
            if f" {m} " in page_text or page_text.startswith(m):
                method = m
                break

        # Look for endpoint URL
        endpoint_match = re.search(r'(https?://[^\s]+api\.zenoti\.com[^\s]*)', page_text)
        if endpoint_match:
            endpoint = endpoint_match.group(1)
        elif '/v1/' in page_text:
            endpoint_match = re.search(r'(/v1/[^\s]+)', page_text)
            if endpoint_match:
                endpoint = endpoint_match.group(1)

        if method:
            md += f"**Method:** `{method}`\n\n"
        if endpoint:
            md += f"**Endpoint:** `{endpoint}`\n\n"

        md += "---\n\n"

        # Extract description
        desc_elem = soup.find('p')
        if desc_elem:
            desc = desc_elem.get_text().strip()
            if desc and len(desc) > 20:
                md += f"## Description\n\n{desc}\n\n"

        # Extract parameters section
        params_section = self._extract_parameters_section(soup)
        if params_section:
            md += params_section

        # Extract code examples (focus on Python)
        code_section = self._extract_code_examples_section()
        if code_section:
            md += code_section

        # Extract response information
        response_section = self._extract_response_section(soup)
        if response_section:
            md += response_section

        # Fallback: if not much content, get visible text
        if len(md) < 300:
            md += "## Content\n\n"
            # Get main content, excluding API tester
            try:
                main_content = self.page.locator("article, main, [class*='content']").first
                if main_content:
                    md += main_content.inner_text()[:5000]
            except Exception:
                md += self._extract_visible_text()[:5000]

        return md

    def _extract_parameters_section(self, soup: BeautifulSoup) -> str:
        """Extract parameters from the page."""
        md = ""

        # Look for parameter sections
        param_headers = soup.find_all(string=re.compile(r'(Body|Query|Path|Header)\s*Param', re.I))

        for header in param_headers:
            section_name = header.strip()
            md += f"## {section_name}\n\n"

            # Find the parent container and extract parameters
            parent = header.find_parent(['div', 'section', 'form'])
            if parent:
                # Look for parameter items
                items = parent.find_all(['label', 'dt', 'span'])
                if items:
                    md += "| Parameter | Type | Required | Description |\n"
                    md += "|-----------|------|----------|-------------|\n"
                    for item in items[:20]:  # Limit to 20 params
                        param_name = item.get_text().strip()
                        if param_name and len(param_name) < 50:
                            md += f"| `{param_name}` | string | - | - |\n"
                    md += "\n"

        return md

    def _extract_code_examples_section(self) -> str:
        """Extract code examples, prioritizing Python."""
        md = ""

        # First, try to click Python tab
        self._click_python_tab()
        time.sleep(0.3)

        # Get all code blocks
        code_blocks = self._extract_code_blocks()

        # Also try clicking through language tabs
        tab_content = self._click_all_tabs_and_extract()

        # Prioritize Python
        python_code = tab_content.get('Python') or tab_content.get('python')
        if not python_code:
            for block in code_blocks:
                if 'import' in block['code'] or 'requests' in block['code']:
                    python_code = block['code']
                    break

        if python_code:
            md += "## Code Examples\n\n"
            md += "### Python\n\n"
            md += f"```python\n{python_code}\n```\n\n"

        # Add cURL if available
        curl_code = tab_content.get('cURL') or tab_content.get('Shell') or tab_content.get('curl')
        if not curl_code:
            for block in code_blocks:
                if 'curl' in block['code'].lower():
                    curl_code = block['code']
                    break

        if curl_code:
            if "## Code Examples" not in md:
                md += "## Code Examples\n\n"
            md += "### cURL\n\n"
            md += f"```bash\n{curl_code}\n```\n\n"

        return md

    def _extract_response_section(self, soup: BeautifulSoup) -> str:
        """Extract response information."""
        md = ""

        # Look for response section
        response_headers = soup.find_all(string=re.compile(r'Response', re.I))

        for header in response_headers[:1]:  # Just first response section
            parent = header.find_parent(['div', 'section'])
            if parent:
                # Look for status codes
                status_codes = parent.find_all(string=re.compile(r'^[245]\d{2}$'))
                if status_codes:
                    md += "## Responses\n\n"
                    for code in status_codes[:5]:
                        desc = "Success" if code.startswith('2') else "Error"
                        md += f"- **{code}**: {desc}\n"
                    md += "\n"

        return md

    def _extract_page_as_markdown(self, url: str, title: str) -> str:
        """Generic page extraction as markdown."""
        self.page.goto(url, timeout=NAV_TIMEOUT)
        self._wait_for_page_load()
        time.sleep(RATE_LIMIT_DELAY)

        # Click Python tab if available
        self._click_python_tab()

        soup = BeautifulSoup(self.page.content(), 'html.parser')

        # Remove script, style, and navigation elements
        for tag in soup.find_all(['script', 'style', 'nav', 'header', 'footer']):
            tag.decompose()

        # Get title from page
        page_title = title
        h1 = soup.find('h1')
        if h1:
            page_title = h1.get_text().strip()

        md = f"# {page_title}\n\n"
        md += f"**Source:** {url}\n\n"
        md += "---\n\n"

        # Convert main content to markdown
        main = soup.find(['main', 'article']) or soup.find('body')
        if main:
            md += self._html_to_markdown(main)

        # Add any code blocks
        code_blocks = self._extract_code_blocks()
        if code_blocks:
            md += "\n## Code Examples\n\n"
            for block in code_blocks[:3]:  # Limit to 3 code blocks
                lang = block.get('language', '')
                md += f"```{lang}\n{block['code']}\n```\n\n"

        return md

    # ========== MAIN RUN ==========

    def run(self):
        """Run the complete scraping process."""
        start_time = datetime.now()
        logger.info("Starting Zenoti documentation scrape")
        logger.info(f"Headless mode: {self.headless}")

        # Create output directories
        for subdir in ["recipes", "reference", "guides"]:
            (self.output_dir / subdir).mkdir(parents=True, exist_ok=True)

        new_manifest = {"files": {}}
        successful = 0
        failed = 0

        with sync_playwright() as p:
            self.browser = p.chromium.launch(headless=self.headless)
            self.page = self.browser.new_page()
            self.page.set_default_timeout(DEFAULT_TIMEOUT)

            # Scrape recipes
            try:
                recipes = self.scrape_recipes_page()
                for filename, content in recipes:
                    if content:
                        filepath = self.output_dir / "recipes" / filename
                        filepath.write_text(content, encoding='utf-8')
                        new_manifest["files"][f"recipes/{filename}"] = {
                            "hash": self._content_hash(content),
                            "last_updated": datetime.now().isoformat(),
                            "source_url": f"{BASE_URL}/recipes"
                        }
                        successful += 1
            except Exception as e:
                logger.error(f"Failed to scrape recipes: {e}")
                failed += 1

            # Scrape guides
            try:
                guides = self.scrape_guides()
                for filename, content in guides:
                    if content:
                        filepath = self.output_dir / "guides" / filename
                        filepath.write_text(content, encoding='utf-8')
                        new_manifest["files"][f"guides/{filename}"] = {
                            "hash": self._content_hash(content),
                            "last_updated": datetime.now().isoformat(),
                            "source_url": f"{BASE_URL}/docs"
                        }
                        successful += 1
            except Exception as e:
                logger.error(f"Failed to scrape guides: {e}")
                failed += 1

            # Scrape reference endpoints
            try:
                references = self.scrape_reference()
                for filename, content in references:
                    if content:
                        filepath = self.output_dir / "reference" / filename
                        filepath.write_text(content, encoding='utf-8')
                        new_manifest["files"][f"reference/{filename}"] = {
                            "hash": self._content_hash(content),
                            "last_updated": datetime.now().isoformat(),
                            "source_url": f"{BASE_URL}/reference"
                        }
                        successful += 1
            except Exception as e:
                logger.error(f"Failed to scrape reference: {e}")
                failed += 1

            self.browser.close()

        # Save manifest
        new_manifest["fetch_metadata"] = {
            "last_fetch_completed": datetime.now().isoformat(),
            "fetch_duration_seconds": (datetime.now() - start_time).total_seconds(),
            "successful": successful,
            "failed": failed,
            "fetch_tool_version": "2.0"
        }
        self._save_manifest(new_manifest)

        # Summary
        duration = datetime.now() - start_time
        logger.info(f"\nScrape completed in {duration}")
        logger.info(f"Successful: {successful}")
        logger.info(f"Failed: {failed}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Scrape Zenoti API documentation")
    parser.add_argument("--visible", action="store_true", help="Run browser in visible mode (not headless)")
    parser.add_argument("--output", type=str, default=None, help="Output directory")
    args = parser.parse_args()

    if args.output:
        docs_dir = Path(args.output)
    else:
        docs_dir = Path(__file__).parent.parent / 'docs'

    scraper = ZenotiDocsScraper(docs_dir, headless=not args.visible)
    scraper.run()


if __name__ == "__main__":
    main()
