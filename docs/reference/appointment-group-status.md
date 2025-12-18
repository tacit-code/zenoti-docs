# Authentication

**Source:** https://docs.zenoti.com/reference/appointment-group-status

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
Appointment Group Created
Appointment Group Status
Employee Events
Guest Package Events
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
Appointment Group Status
Sample Response Object – Appointment Group Status
Appointment Group Status
{
  "id": "62399ceda961750e01dd99f6",
  "event_id": "62399ceda961750e01dd99f5",
  "event_schema": "v1",
  "event_resource": "AppointmentGroup",
  "event_type": "AppointmentGroup.Status",
  "event_timestamp": "2022-03-22T09:54:53.3484785Z",
  "data": {
    "invoice_id": "7f7f7bc0-813a-4a24-b518-b8bc67b63de6",
    "invoice_number": "13024",
    "receipt_number": "0",
    "appointment_group_id": "53ef8c73-ded2-48cf-b6b2-0492a0463f9b",
    "appointment_group_status": 2,
    "is_noshowfeerequired": "Yes",
    "is_cancellationfeerequired": "Yes"
  }
}


Updated over 3 years ago

Appointment Group Created
Employee Events
Did this page help you?
Yes
No
TABLE OF CONTENTS
Sample Response Object – Appointment Group Status