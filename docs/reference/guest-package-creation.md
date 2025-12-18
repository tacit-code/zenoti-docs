# Authentication

**Source:** https://docs.zenoti.com/reference/guest-package-creation

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
Guest Package Creation
Sample Object Response – Guest Package Creation
Guest Package Creation
{
    "user_package_id": "fe645486-7165-41de-8948-7f476c856824",
    "status": 1,
    "user_package_state": 2,
    "invoice": {
        "status": 0,
        "receipt_no": "0",
        "id": "4ed8572b-daaf-496a-8e36-aa27e8399917",
        "no": "RR16674"
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
        "date": "2022-03-02T05:26:34"
    },
    "date": {
        "end_date_with_grace": "2022-04-26T00:00:00",
        "start": "2022-03-02T00:00:00",
        "end": "2022-04-01T00:00:00"
    },
    "schedule": {
        "completed_schedules": 1,
        "next_schedule_date": "2022-03-03T20:00:00"
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
    "services": [
        {
            "service_type_info": {
                "service_category_type": 2,
                "id": "d259ba65-2eec-42ca-8670-4b35c00ffd06",
                "name": "Aroma Body Massage",
                "duration": 15,
                "has_segments": false
            },
            "exists_in_current_center": true,
            "total": 1,
            "used": 0,
            "balance": 0,
            "balance_amount": 0,
            "price": null,
            "package_service_price": 0.86,
            "sale_as_part_of_package_or_membership_only": false,
            "book_with_partial_balance": 1
        },
        {
            "service_type_info": {
                "service_category_type": 2,
                "id": "1826509a-c7dc-457c-9a9a-e2c921965847",
                "name": "Oxy Facial Massage",
                "duration": 30,
                "has_segments": true
            },
            "exists_in_current_center": true,
            "total": 1,
            "used": 0,
            "balance": 1,
            "balance_amount": 51.72,
            "price": null,
            "package_service_price": 51.72,
            "sale_as_part_of_package_or_membership_only": false,
            "book_with_partial_balance": 1
        },
        {
            "service_type_info": {
                "service_category_type": 1,
                "id": "977b2015-b764-452a-9562-a45a309ffcbe",
                "name": "Coloring",
                "duration": 0,
                "has_segments": false
            },
            "exists_in_current_center": true,
            "total": 2,
            "used": 0,
            "balance": 2,
            "balance_amount": 2.06,
            "price": null,
            "package_service_price": 1.03,
            "sale_as_part_of_package_or_membership_only": null,
            "book_with_partial_balance": 1
        },
        {
            "service_type_info": {
                "service_category_type": 3,
                "id": "c35f8a2b-af2a-4bac-9bf7-7490c82580b1",
                "name": "Servic tag",
                "duration": 0,
                "has_segments": false
            },
            "exists_in_current_center": true,
            "total": 1,
            "used": 0,
            "balance": 1,
            "balance_amount": 11.38,