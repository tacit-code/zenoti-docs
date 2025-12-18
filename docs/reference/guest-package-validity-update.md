# Authentication

**Source:** https://docs.zenoti.com/reference/guest-package-validity-update

---

## Content

Jump to Content
Log In
v1.0
Guides
Recipes
API Reference
API Changelog
Search
CTRL-K
JUMP TO
CTRL-/
AUTHENTICATION
Access Tokens
CENTERS
Center APIs
Center - Categories
Center - Rooms
Center - Employees
Center - Services
Center - Packages
Center - Products
Center - Memberships
GUESTS
Add V1 online guest creation
POST
Guest APIs
Guest Notes
Guest Form
Guest Memberships
Guest Password
EMPLOYEES
Employee APIs
BlockOut Times
Security Roles
ROOMS
BlockOut Times
SERVICE BOOKING
Service Booking APIs
GIFT CARDS
Gift Card APIs
Gift Card Templates
OPPORTUNITIES
Opportunities APIs
Notes
APPOINTMENTS
Appointment APIs
ORGANIZATIONS
Organization APIs
REPORTS
Reports APIs
VENDORS
Vendor APIs
INVENTORY
Inventory APIs
CLASSES
Registration
Operations
Consumer
Metrics
SHOPIFY
Shopify APIs
INVOICES
Invoice APIs
Group Invoices
Membership Invoices
Product Invoices
Package Invoices
Invoice Payments
QUEUE
Queue APIs
WEBHOOK EVENTS
Webhook Events
Invoice Events
Guest Events
Classes Schedule Events
Classes Booking Events
Guest Membership Events
Appointment Events
Appointment Feedback Event
Appointment Group Events
Employee Events
Guest Package Events
Guest Package Creation
Guest Package Redemption
Guest Package Redemption Reversal
Guest Package Status Update
Guest Package Validity Update
EPRESCRIBE
Validate NPI details of a prescriber
PUT
DIGITAL FORMS
Retrieve compliance statistics
GET
Get guest consent for ZenScribe
GET
Add guest consent for ZenScribe
POST
Powered by 
Guest Package Validity Update
Sample Response Code – Guest Package Validity Update
Guest Package Validity Update
{
    "user_package_id": "0cc3f6bd-680e-4953-bda6-9441565efb52",
    "status": 1,
    "user_package_state": 0,
    "invoice": {
        "status": 4,
        "receipt_no": "RRR6059",
        "id": "1ee272c2-bb54-4350-87d3-f32ac034aacc",
        "no": "RR16675"
    },
    "package": {
        "code": "15 min facial package",
        "is_OTP_required": false,
        "type": 0,
        "id": "e19e0f53-74d3-46b7-bc87-bef8fbc185c8",
        "name": "15 min facial package"
    },
    "purchase": {
        "price": {
            "currency_id": 0,
            "sales": 0,
            "tax": 0,
            "final": 110
        },
        "date": "2022-03-02T05:55:14"
    },
    "date": {
        "end_date_with_grace": "2022-04-26T09:55:25",
        "start": "2022-03-02T09:55:25",
        "end": "2022-04-01T09:55:25"
    },
    "schedule": {
        "completed_schedules": null,
        "next_schedule_date": null
    },
    "center": {
        "id": "a11f578a-1b81-4de0-8834-915f79e5362b",
        "name": "Khammam"
    },
    "is_refunded": false,
    "sale_invoice": {
        "id": null,
        "no": null
    },
    "lookup_package_user_id": null,
    "start_validity_at_first_redemption": false,
    "never_expires": false,
    "has_first_redemption": true,
    "expiration_days": 30
}


Updated over 3 years ago

Guest Package Status Update
Validate NPI details of a prescriber
Did this page help you?
Yes
No
TABLE OF CONTENTS
Sample Response Code – Guest Package Validity Update