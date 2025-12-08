# Zenoti API Documentation Mirror

A documentation scraper and mirror for [docs.zenoti.com](https://docs.zenoti.com), designed for offline access with Claude Code.

## Overview

This repository automatically scrapes and mirrors Zenoti's API documentation, converting it to markdown format for easy reference. The scraper uses Playwright for browser automation since Zenoti's documentation is built on ReadMe.io, which renders content with JavaScript.

## Features

- **Automated Updates** - GitHub Actions workflow refreshes documentation every 12 hours
- **Three Content Types** - Recipes (workflows), Guides (concepts), and API Reference
- **Code Examples** - Extracts Python and cURL examples from interactive tabs
- **Manifest Tracking** - SHA256 hashes detect content changes
- **Claude Code Integration** - Includes CLAUDE.md for seamless AI-assisted development

## Installation

### Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/tacit-code/zenoti-docs/main/install.sh | bash
```

### Manual Install

```bash
git clone https://github.com/tacit-code/zenoti-docs.git ~/.zenoti-docs
```

### Uninstall

```bash
~/.zenoti-docs/uninstall.sh
```

## Usage with Claude Code

Add this to your project's `CLAUDE.md`:

```markdown
Reference Zenoti API docs at: ~/.zenoti-docs/docs/

Key documentation:
- Booking workflow: ~/.zenoti-docs/docs/recipes/online-booking-workflow.md
- Authentication: ~/.zenoti-docs/docs/guides/authentication.md
- API Reference: ~/.zenoti-docs/docs/reference/
```

## Documentation Structure

```
docs/
├── recipes/                    # Complete workflow examples with Python code
│   ├── online-booking-workflow.md
│   ├── create-opportunity.md
│   ├── sale-of-membership.md
│   ├── sale-of-package.md
│   └── ...
├── guides/                     # Conceptual documentation
│   ├── overview.md
│   ├── authentication.md
│   ├── pagination.md
│   ├── error-codes.md
│   └── ...
├── reference/                  # API endpoint documentation
│   ├── generate-access-token.md
│   ├── create-a-guest.md
│   ├── service-booking.md
│   └── ...
└── docs_manifest.json          # Tracking manifest
```

## Running the Scraper Locally

### Prerequisites

- Python 3.11+
- Playwright with Chromium

### Setup

```bash
cd ~/.zenoti-docs
pip install -r scripts/requirements.txt
playwright install chromium
playwright install-deps
```

### Run

```bash
python scripts/fetch_zenoti_docs.py
```

## Common Implementation Notes

When building Zenoti integrations, be aware of these common issues:

| Issue | Solution |
|-------|----------|
| Two-step booking | Booking requires slot reservation then confirmation |
| Gender codes | Male=1, Female=2, Other=0 |
| Guest updates | Preserve existing data when updating password |
| Slot reservation | Must reserve before confirming booking |

## GitHub Actions

The workflow runs automatically:
- **Schedule**: Every 12 hours (0:00 and 12:00 UTC)
- **Manual**: Can be triggered via workflow_dispatch

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT

## Disclaimer

This is an unofficial mirror. All documentation content is owned by Zenoti. This project is not affiliated with or endorsed by Zenoti.
