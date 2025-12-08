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
