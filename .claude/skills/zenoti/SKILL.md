---
name: zenoti
description: This skill provides guidance for integrating with the Zenoti API for salon, spa, and wellness business management. Use this skill when building booking systems, guest management, appointment scheduling, membership sales, or any integration with Zenoti's platform. The skill includes authentication patterns, common workflows, and references to scraped API documentation.
---

# Zenoti API Integration

## Overview

Zenoti is a cloud-based business management platform for salons, spas, and wellness centers. This skill enables building reliable integrations with Zenoti's REST API, covering authentication, guest management, service booking, and payment workflows.

## Documentation Location

Complete scraped API documentation is available at:
```
~/.zenoti-docs/docs/
├── recipes/      # Complete workflow examples (9 files)
├── guides/       # Conceptual documentation (36 files)
└── reference/    # API endpoint docs (311 files)
```

To find specific endpoints, use grep:
```bash
grep -r "keyword" ~/.zenoti-docs/docs/reference/
```

## Authentication

Zenoti supports two authentication methods:

### API Key (Server-to-Server)
```
Header: Authorization: apikey {api_key}
```
- Best for backend integrations
- No expiration (until revoked)
- Access to all APIs

### Token-Based (User Context)
```
Header: Authorization: bearer {access_token}
```
- Best for user-facing apps
- Tokens expire (use refresh token)
- Role-based access control

To generate tokens, see: `~/.zenoti-docs/docs/reference/generate-an-access-token.md`

## Critical Implementation Notes

These issues have caused integration failures:

| Issue | Correct Implementation |
|-------|----------------------|
| Gender codes | Male=1, Female=2, Other=0 |
| Two-step booking | Must call reserve-slot THEN confirm-booking |
| Guest updates | Preserve all existing fields when updating password |
| Slot reservation | Reservation expires - confirm within time window |

## Core Workflows

### 1. Service Booking Flow

The booking process requires these steps in order:

1. **Authenticate** → Get access token
2. **Search guest** → `search-for-a-guest.md`
3. **Create guest** (if new) → `create-a-guest.md`
4. **Get available slots** → `retrieve-available-slots-for-a-service-booking.md`
5. **Reserve slot** → `reserve-a-slot-for-a-service-booking.md`
6. **Confirm booking** → `confirm-a-service-booking.md`

Reference: `~/.zenoti-docs/docs/recipes/online-booking-workflow-for-guests.md`

### 2. Guest Management

| Action | Endpoint Reference |
|--------|-------------------|
| Search | `search-for-a-guest.md` |
| Create | `create-a-guest.md` |
| Update | `update-a-guest.md` |
| Get details | `retrieve-guest-details.md` |
| List all | `list-all-guests-of-a-center.md` |

### 3. Membership Sales

1. Create invoice → `create-an-invoice-for-memberships.md`
2. Add membership → `add-a-membership-to-an-invoice.md`
3. Collect payment → `collect-invoice-payment-by-using-a-guests-saved-creditdebit-card.md`
4. Close invoice → `close-a-membership-sale-invoice.md`

## Common Endpoints Quick Reference

### Authentication
- `generate-an-access-token.md`
- `refresh-an-access-token.md`
- `revoke-an-existing-access-token.md`

### Centers & Services
- `list-all-centers.md`
- `list-all-services-of-a-center.md`
- `list-all-therapists-of-a-center.md`

### Appointments
- `list-all-appointments-of-a-guest.md`
- `retrieve-the-details-of-an-appointment.md`
- `cancel-a-service-booking.md`
- `reschedule-a-service-booking.md`

### Invoices
- `retrieve-invoice-details.md`
- `close-an-invoice.md`
- `invoice-payments.md`

## Error Handling

Common HTTP status codes:
- 200: Success
- 400: Bad request (check parameters)
- 401: Authentication failed
- 403: Permission denied (check user role)
- 404: Resource not found
- 429: Rate limited

## Finding Documentation

To locate specific API documentation:

```bash
# Find booking-related endpoints
ls ~/.zenoti-docs/docs/reference/ | grep -i book

# Find guest endpoints
ls ~/.zenoti-docs/docs/reference/ | grep -i guest

# Search content for specific terms
grep -l "center_id" ~/.zenoti-docs/docs/reference/*.md
```

## Resources

### references/
- `api-index.md` - Categorized index of all 311 API endpoints
- `common-patterns.md` - Reusable code patterns for Zenoti integrations

To read reference docs:
```bash
cat ~/.zenoti-docs/docs/reference/{endpoint-name}.md
```
