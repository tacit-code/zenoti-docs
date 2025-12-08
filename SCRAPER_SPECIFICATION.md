Zenoti API Documentation Mirror - Complete Specification
Scraper Specification (SCRAPER_SPECIFICATION.md)

# Zenoti Docs Scraper Specification

## Overview

This specification outlines how to build a documentation scraper for `docs.zenoti.com` that mirrors the approach used by `ericbuess/claude-code-docs`, adapted for Zenoti's ReadMe.io-based documentation platform.

## Key Differences from claude-code-docs

| Aspect | claude-code-docs | zenoti-docs |
|--------|------------------|-------------|
| Platform | Anthropic docs (direct .md URLs) | ReadMe.io (JavaScript-rendered) |
| Content Access | `{url}.md` endpoint | Requires browser automation |
| Sitemap | Available at `/sitemap.xml` | May not be publicly accessible |
| Code Examples | Embedded in markdown | Dynamic tabs (Python, cURL, etc.) |
| Structure | Flat documentation | Recipes (interactive), Reference (API), Guides |

## Architecture
```
zenoti-docs/
├── .github/
│   └── workflows/
│       └── fetch-docs.yml          # GitHub Actions workflow
├── scripts/
│   ├── fetch_zenoti_docs.py        # Main scraper (Playwright-based)
│   ├── requirements.txt            # Python dependencies
│   └── zenoti-docs-helper.sh.template
├── docs/
│   ├── recipes/                    # Python workflow examples
│   │   ├── online-booking-workflow.md
│   │   ├── create-opportunity.md
│   │   ├── sale-of-membership.md
│   │   ├── sale-of-package.md
│   │   ├── sale-of-gift-card.md
│   │   ├── google-ads-offline-conversion.md
│   │   ├── extract-purchase-orders.md
│   │   └── employee-profiles-management.md
│   ├── reference/                  # API endpoint documentation
│   │   ├── authentication/
│   │   │   ├── generate-access-token.md
│   │   │   ├── refresh-access-token.md
│   │   │   └── revoke-access-token.md
│   │   ├── centers/
│   │   ├── guests/
│   │   ├── employees/
│   │   ├── bookings/
│   │   ├── invoices/
│   │   └── webhooks/
│   ├── guides/                     # Conceptual documentation
│   │   ├── overview.md
│   │   ├── getting-started.md
│   │   ├── authentication.md
│   │   ├── pagination.md
│   │   ├── error-codes.md
│   │   ├── rate-limits.md
│   │   └── workflows/
│   │       ├── service-booking.md
│   │       ├── product-sale.md
│   │       ├── membership-sale.md
│   │       └── gift-card-sale.md
│   └── docs_manifest.json          # Manifest tracking all files
├── CLAUDE.md                       # Claude Code instructions
├── README.md                       # Repository documentation
├── install.sh                      # Installation script
└── uninstall.sh                    # Uninstallation script
```

## Dependencies
```txt
# requirements.txt
playwright>=1.40.0
beautifulsoup4>=4.12.0
requests>=2.31.0
```

## Scraper Implementation

### fetch_zenoti_docs.py
```python
#!/usr/bin/env python3
"""
Zenoti API Documentation Scraper

Scrapes documentation from docs.zenoti.com using Playwright for 
browser automation (required due to ReadMe.io's JavaScript rendering).

Key differences from claude-code-docs scraper:
1. Uses Playwright instead of requests (JavaScript-rendered content)
2. Handles interactive recipe dialogs
3. Extracts code from tabbed interfaces
4. Processes API reference forms and schemas
"""

import json
import hashlib
import logging
import re
import time
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional
from urllib.parse import urljoin, urlparse

from playwright.sync_api import sync_playwright, Page, Browser
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
RATE_LIMIT_DELAY = 1.0  # seconds between requests
MAX_RETRIES = 3

# Content sections to scrape
SECTIONS = {
    "recipes": {
        "url": "/recipes",
        "items": [
            "online-booking-workflow-for-guests",
            "create-an-opportunity-in-sales-module", 
            "sale-of-a-membership",
            "sale-of-a-package",
            "sale-of-a-gift-card",
            "google-ads-offline-conversion",
            "extract-purchase-orders",
            "employee-profiles-management"
        ]
    },
    "guides": {
        "url": "/docs",
        "items": [
            "overview",
            "create-the-backend-app-and-generate-a-new-api-key",
            "authentication",
            "zenoti-api-groups-1",
            "pagination", 
            "response-and-error-codes",
            "api-rate-limits-1",
            "service-booking-apis",
            "product-sale-apis",
            "membership-sale-apis",
            "gift-card-sale-apis",
            "opportunity-apis"
        ]
    },
    "reference": {
        "url": "/reference",
        "categories": [
            "authentication",
            "centers", 
            "guests",
            "employees",
            "rooms",
            "service-booking",
            "gift-cards",
            "opportunities",
            "appointments",
            "organizations",
            "reports",
            "invoices",
            "classes",
            "webhook-events"
        ]
    }
}


class ZenotiDocsScraper:
    """Scraper for Zenoti API documentation."""
    
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.manifest = self._load_manifest()
        self.browser: Optional[Browser] = None
        self.page: Optional[Page] = None
        
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
    
    def _wait_for_content(self, selector: str, timeout: int = 10000) -> bool:
        """Wait for content to load."""
        try:
            self.page.wait_for_selector(selector, timeout=timeout)
            return True
        except Exception:
            return False
    
    def scrape_recipe(self, recipe_slug: str) -> Tuple[str, str]:
        """
        Scrape a recipe page with all steps and Python code.
        
        Recipes are interactive dialogs that need to be opened and 
        stepped through to extract all content.
        """
        logger.info(f"Scraping recipe: {recipe_slug}")
        
        # Navigate to recipes page
        self.page.goto(f"{BASE_URL}/recipes")
        self._wait_for_content("main")
        time.sleep(RATE_LIMIT_DELAY)
        
        # Find and click the recipe to open dialog
        recipe_button = self.page.locator(f"text='{recipe_slug}'").first
        if not recipe_button:
            # Try finding by heading
            recipe_button = self.page.locator(f"heading:has-text('{recipe_slug}')").first
        
        # Click "Open Recipe" button for this recipe
        recipe_card = self.page.locator(f"listitem:has-text('{recipe_slug}')")
        open_button = recipe_card.locator("button:has-text('Open Recipe')")
        open_button.click()
        
        # Wait for dialog to open
        self._wait_for_content("dialog")
        time.sleep(0.5)
        
        # Click Python tab to ensure we get Python code
        python_tab = self.page.locator("button:has-text('Python')").first
        if python_tab:
            python_tab.click()
            time.sleep(0.3)
        
        # Extract recipe title and description
        title = self.page.locator("dialog heading").first.text_content()
        description = self.page.locator("dialog >> text=/This recipe/").first.text_content()
        
        # Extract all steps
        steps = []
        step_buttons = self.page.locator("dialog form button").all()
        
        for i, step_btn in enumerate(step_buttons):
            step_btn.click()
            time.sleep(0.3)
            
            # Get step title and description
            step_banner = step_btn.locator("banner").first
            step_title = step_banner.text_content() if step_banner else f"Step {i+1}"
            step_desc = step_btn.locator("generic").last.text_content()
            
            # Get the code for this step (visible in code panel)
            code_content = self._extract_code_content()
            
            steps.append({
                "number": i + 1,
                "title": step_title,
                "description": step_desc,
                "code": code_content
            })
        
        # Extract full Python code using Copy button
        copy_button = self.page.locator("dialog button:has-text('Copy')").first
        if copy_button:
            copy_button.click()
            # Code is now in clipboard - we'll reconstruct from visible content
        
        # Get full code from the code panel
        full_code = self._extract_full_code()
        
        # Close dialog
        close_button = self.page.locator("button:has-text('Close Recipe')")
        if close_button:
            close_button.click()
        
        # Generate markdown
        markdown = self._recipe_to_markdown(title, description, steps, full_code)
        filename = f"{self._slugify(recipe_slug)}.md"
        
        return filename, markdown
    
    def _extract_code_content(self) -> str:
        """Extract code from the code panel."""
        code_lines = []
        presentations = self.page.locator("dialog presentation").all()
        for pres in presentations:
            text = pres.text_content()
            if text and text.strip():
                code_lines.append(text)
        return "\\n".join(code_lines)
    
    def _extract_full_code(self) -> str:
        """Extract the complete Python code from recipe."""
        # The code is in a textbox or code block
        code_element = self.page.locator("dialog textbox").first
        if code_element:
            return code_element.input_value()
        
        # Alternative: reconstruct from presentation elements
        return self._extract_code_content()
    
    def _recipe_to_markdown(self, title: str, description: str, 
                           steps: List[dict], full_code: str) -> str:
        """Convert recipe data to markdown format."""
        md = f"# {title}\\n\\n"
        md += f"> {description}\\n\\n"
        md += f"**Source:** https://docs.zenoti.com/recipes\\n\\n"
        md += "---\\n\\n"
        
        # Table of contents
        md += "## Workflow Steps\\n\\n"
        md += "| Step | Title | Description |\\n"
        md += "|------|-------|-------------|\\n"
        for step in steps:
            md += f"| {step['number']} | {step['title']} | {step['description'][:80]}... |\\n"
        md += "\\n---\\n\\n"
        
        # Detailed steps
        for step in steps:
            md += f"## Step {step['number']}: {step['title']}\\n\\n"
            md += f"{step['description']}\\n\\n"
            if step.get('code'):
                md += "```python\\n"
                md += step['code']
                md += "\\n```\\n\\n"
        
        # Full code
        md += "---\\n\\n"
        md += "## Complete Python Implementation\\n\\n"
        md += "```python\\n"
        md += full_code
        md += "\\n```\\n"
        
        return md
    
    def scrape_reference_endpoint(self, endpoint_path: str) -> Tuple[str, str]:
        """
        Scrape an API reference endpoint page.
        
        Extracts: method, URL, description, parameters, request/response schemas.
        """
        logger.info(f"Scraping reference: {endpoint_path}")
        
        url = f"{BASE_URL}/reference/{endpoint_path}"
        self.page.goto(url)
        self._wait_for_content("article")
        time.sleep(RATE_LIMIT_DELAY)
        
        # Extract page content
        soup = BeautifulSoup(self.page.content(), 'html.parser')
        
        # Get title
        title_elem = soup.select_one("article heading")
        title = title_elem.text if title_elem else endpoint_path
        
        # Get HTTP method and URL
        method_elem = soup.select_one("generic:contains('post'), generic:contains('get'), generic:contains('put'), generic:contains('delete')")
        method = method_elem.text.upper() if method_elem else "GET"
        
        url_elem = soup.select_one("generic:contains('api.zenoti.com')")
        api_url = url_elem.text if url_elem else ""
        
        # Get description
        desc_elem = soup.select_one("article banner generic:contains('Purpose')")
        description = ""
        if desc_elem:
            description = desc_elem.find_next_sibling().text if desc_elem.find_next_sibling() else ""
        
        # Get parameters
        params = self._extract_parameters(soup)
        
        # Get response schema
        responses = self._extract_responses(soup)
        
        # Get code examples
        code_examples = self._extract_code_examples()
        
        # Generate markdown
        markdown = self._reference_to_markdown(
            title, method, api_url, description, 
            params, responses, code_examples
        )
        filename = f"{self._slugify(endpoint_path)}.md"
        
        return filename, markdown
    
    def _extract_parameters(self, soup: BeautifulSoup) -> List[dict]:
        """Extract API parameters from page."""
        params = []
        param_section = soup.select_one("form banner:contains('Body Params')")
        if param_section:
            form = param_section.find_parent("form")
            if form:
                labels = form.select("label")
                for label in labels:
                    param_name = label.text
                    param_type = label.find_next_sibling("generic")
                    param_required = label.find_next("generic:contains('required')")
                    param_desc = label.find_next("generic", class_=lambda x: x and "desc" in str(x).lower())
                    
                    params.append({
                        "name": param_name,
                        "type": param_type.text if param_type else "string",
                        "required": bool(param_required),
                        "description": param_desc.text if param_desc else ""
                    })
        return params
    
    def _extract_responses(self, soup: BeautifulSoup) -> List[dict]:
        """Extract response schemas from page."""
        responses = []
        response_section = soup.select_one("banner:contains('Responses')")
        if response_section:
            response_buttons = soup.select("heading:contains('200'), heading:contains('400'), heading:contains('401')")
            for btn in response_buttons:
                code = btn.text[:3]
                responses.append({
                    "code": code,
                    "description": "Success" if code == "200" else "Error"
                })
        return responses
    
    def _extract_code_examples(self) -> Dict[str, str]:
        """Extract code examples in different languages."""
        examples = {}
        
        # Click Python tab
        python_btn = self.page.locator("button:has-text('Python')").first
        if python_btn:
            python_btn.click()
            time.sleep(0.3)
            code = self.page.locator("region textbox").first
            if code:
                examples["python"] = code.input_value()
        
        # Click Shell/cURL tab
        shell_btn = self.page.locator("button:has-text('Shell')").first
        if shell_btn:
            shell_btn.click()
            time.sleep(0.3)
            code = self.page.locator("region textbox").first
            if code:
                examples["curl"] = code.input_value()
        
        return examples
    
    def _reference_to_markdown(self, title: str, method: str, api_url: str,
                               description: str, params: List[dict],
                               responses: List[dict], code_examples: Dict[str, str]) -> str:
        """Convert API reference data to markdown."""
        md = f"# {title}\\n\\n"
        md += f"**Method:** `{method}`\\n\\n"
        md += f"**Endpoint:** `{api_url}`\\n\\n"
        md += f"**Source:** https://docs.zenoti.com/reference/{self._slugify(title)}\\n\\n"
        
        if description:
            md += f"## Description\\n\\n{description}\\n\\n"
        
        if params:
            md += "## Parameters\\n\\n"
            md += "| Name | Type | Required | Description |\\n"
            md += "|------|------|----------|-------------|\\n"
            for p in params:
                req = "Yes" if p['required'] else "No"
                md += f"| `{p['name']}` | {p['type']} | {req} | {p['description'][:60]} |\\n"
            md += "\\n"
        
        if responses:
            md += "## Responses\\n\\n"
            for r in responses:
                md += f"- **{r['code']}**: {r['description']}\\n"
            md += "\\n"
        
        if code_examples:
            md += "## Code Examples\\n\\n"
            if "python" in code_examples:
                md += "### Python\\n\\n```python\\n"
                md += code_examples["python"]
                md += "\\n```\\n\\n"
            if "curl" in code_examples:
                md += "### cURL\\n\\n```bash\\n"
                md += code_examples["curl"]
                md += "\\n```\\n\\n"
        
        return md
    
    def scrape_guide(self, guide_path: str) -> Tuple[str, str]:
        """Scrape a guide/documentation page."""
        logger.info(f"Scraping guide: {guide_path}")
        
        url = f"{BASE_URL}/docs/{guide_path}"
        self.page.goto(url)
        self._wait_for_content("article")
        time.sleep(RATE_LIMIT_DELAY)
        
        # Get page HTML
        soup = BeautifulSoup(self.page.content(), 'html.parser')
        
        # Extract article content
        article = soup.select_one("article")
        if not article:
            return "", ""
        
        # Get title
        title = article.select_one("heading")
        title_text = title.text if title else guide_path
        
        # Get main content
        content_parts = []
        for elem in article.select("heading, generic, list, table"):
            if elem.name == "heading":
                level = len(elem.get("class", [])) + 1
                content_parts.append(f"{'#' * min(level, 6)} {elem.text}\\n")
            elif elem.name == "list":
                for li in elem.select("listitem"):
                    content_parts.append(f"- {li.text}\\n")
            elif elem.name == "table":
                # Convert table to markdown
                content_parts.append(self._table_to_markdown(elem))
            else:
                text = elem.text.strip()
                if text and len(text) > 10:
                    content_parts.append(f"{text}\\n\\n")
        
        markdown = f"# {title_text}\\n\\n"
        markdown += f"**Source:** {url}\\n\\n"
        markdown += "---\\n\\n"
        markdown += "".join(content_parts)
        
        filename = f"{self._slugify(guide_path)}.md"
        return filename, markdown
    
    def _table_to_markdown(self, table_elem) -> str:
        """Convert HTML table to markdown."""
        rows = table_elem.select("tr, generic")
        if not rows:
            return ""
        
        md = "\\n"
        for i, row in enumerate(rows):
            cells = row.select("td, th, generic")
            if cells:
                md += "| " + " | ".join(c.text for c in cells) + " |\\n"
                if i == 0:
                    md += "|" + "|".join("---" for _ in cells) + "|\\n"
        return md + "\\n"
    
    def _slugify(self, text: str) -> str:
        """Convert text to URL-safe slug."""
        text = text.lower()
        text = re.sub(r'[^\\w\\s-]', '', text)
        text = re.sub(r'[-\\s]+', '-', text)
        return text.strip('-')
    
    def run(self):
        """Run the complete scraping process."""
        start_time = datetime.now()
        logger.info("Starting Zenoti documentation scrape")
        
        # Create output directories
        for subdir in ["recipes", "reference", "guides"]:
            (self.output_dir / subdir).mkdir(parents=True, exist_ok=True)
        
        new_manifest = {"files": {}}
        successful = 0
        failed = 0
        
        with sync_playwright() as p:
            self.browser = p.chromium.launch(headless=True)
            self.page = self.browser.new_page()
            
            # Scrape recipes
            logger.info("Scraping recipes...")
            for recipe in SECTIONS["recipes"]["items"]:
                try:
                    filename, content = self.scrape_recipe(recipe)
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
                    logger.error(f"Failed to scrape recipe {recipe}: {e}")
                    failed += 1
            
            # Scrape guides
            logger.info("Scraping guides...")
            for guide in SECTIONS["guides"]["items"]:
                try:
                    filename, content = self.scrape_guide(guide)
                    if content:
                        filepath = self.output_dir / "guides" / filename
                        filepath.write_text(content, encoding='utf-8')
                        new_manifest["files"][f"guides/{filename}"] = {
                            "hash": self._content_hash(content),
                            "last_updated": datetime.now().isoformat(),
                            "source_url": f"{BASE_URL}/docs/{guide}"
                        }
                        successful += 1
                except Exception as e:
                    logger.error(f"Failed to scrape guide {guide}: {e}")
                    failed += 1
            
            # Scrape reference endpoints (key ones)
            logger.info("Scraping API reference...")
            key_endpoints = [
                "generate-an-access-token",
                "refresh-an-access-token",
                "create-a-guest",
                "search-for-a-guest",
                "list-all-centers",
                "create-a-service-booking-copy",
                "reserve-a-slot-for-a-service-booking",
                "confirm-a-service-booking",
                "create-an-invoice-for-memberships",
                "webhook-events"
            ]
            
            for endpoint in key_endpoints:
                try:
                    filename, content = self.scrape_reference_endpoint(endpoint)
                    if content:
                        filepath = self.output_dir / "reference" / filename
                        filepath.write_text(content, encoding='utf-8')
                        new_manifest["files"][f"reference/{filename}"] = {
                            "hash": self._content_hash(content),
                            "last_updated": datetime.now().isoformat(),
                            "source_url": f"{BASE_URL}/reference/{endpoint}"
                        }
                        successful += 1
                except Exception as e:
                    logger.error(f"Failed to scrape endpoint {endpoint}: {e}")
                    failed += 1
            
            self.browser.close()
        
        # Save manifest
        new_manifest["fetch_metadata"] = {
            "last_fetch_completed": datetime.now().isoformat(),
            "fetch_duration_seconds": (datetime.now() - start_time).total_seconds(),
            "successful": successful,
            "failed": failed,
            "fetch_tool_version": "1.0"
        }
        self._save_manifest(new_manifest)
        
        # Summary
        duration = datetime.now() - start_time
        logger.info(f"\\nScrape completed in {duration}")
        logger.info(f"Successful: {successful}")
        logger.info(f"Failed: {failed}")


def main():
    """Main entry point."""
    docs_dir = Path(__file__).parent.parent / 'docs'
    scraper = ZenotiDocsScraper(docs_dir)
    scraper.run()


if __name__ == "__main__":
    main()
```

## GitHub Actions Workflow
```yaml
# .github/workflows/fetch-docs.yml
name: Fetch Zenoti Documentation

on:
  schedule:
    - cron: '0 */12 * * *'  # Every 12 hours
  workflow_dispatch:  # Manual trigger

jobs:
  fetch-docs:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          
      - name: Install dependencies
        run: |
          pip install playwright beautifulsoup4
          playwright install chromium
          playwright install-deps
          
      - name: Run scraper
        run: python scripts/fetch_zenoti_docs.py
        
      - name: Commit and push changes
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add docs/
          git diff --staged --quiet || git commit -m "Update Zenoti docs - $(date -u +%Y-%m-%dT%H:%M:%SZ)"
          git push
```

## Installation Script
```bash
#!/bin/bash
# install.sh - Install zenoti-docs for Claude Code

set -e

REPO_URL="https://github.com/tacit-code/zenoti-docs"
INSTALL_DIR="$HOME/.zenoti-docs"

echo "Installing Zenoti API Documentation..."

# Clone or update repository
if [ -d "$INSTALL_DIR" ]; then
    echo "Updating existing installation..."
    cd "$INSTALL_DIR"
    git pull
else
    echo "Cloning repository..."
    git clone "$REPO_URL" "$INSTALL_DIR"
fi

# Create symlink in common locations
if [ -d "$HOME/.claude" ]; then
    ln -sf "$INSTALL_DIR/docs" "$HOME/.claude/zenoti-docs"
fi

echo ""
echo "Installation complete!"
echo ""
echo "Usage with Claude Code:"
echo "  Add to your CLAUDE.md:"
echo "    Reference Zenoti API docs at: ~/.zenoti-docs/docs/"
echo ""
echo "  Or use the /zenoti command if configured."
```

## CLAUDE.md Template
```markdown
# Zenoti API Documentation

This repository contains mirrored documentation from docs.zenoti.com for offline access with Claude Code.

## Quick Reference

When implementing Zenoti integrations, reference these docs:

### Recipes (Complete Workflows)
- `docs/recipes/online-booking-workflow.md` - **Full booking workflow with 14 steps**
- `docs/recipes/create-opportunity.md` - Sales opportunity creation
- `docs/recipes/sale-of-membership.md` - Membership sales workflow
- `docs/recipes/sale-of-package.md` - Package sales workflow

### API Reference
- `docs/reference/generate-access-token.md` - Authentication
- `docs/reference/create-a-guest.md` - Guest management
- `docs/reference/service-booking.md` - Booking endpoints

### Guides
- `docs/guides/authentication.md` - Auth overview
- `docs/guides/service-booking-workflow.md` - Booking flow

## Slash Commands

/zenoti - List available Zenoti documentation
/zenoti-booking - Show online booking workflow reference
/zenoti-auth - Show authentication documentation

## Common Implementation Issues

Previous implementations have failed due to:
1. Missing the two-step booking ID creation
2. Incorrect gender code mapping (Male=1, Female=2, Other=0)
3. Not preserving guest data when updating password
4. Wrong slot reservation flow

Always reference the recipe docs for the correct implementation.
```