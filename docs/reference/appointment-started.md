# Authentication

**Source:** https://docs.zenoti.com/reference/appointment-started

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
Appointment Started
Appointment Completed
Appointment Feedback Event
Appointment Group Events
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
Appointment Started
Sample Response Code – Appointment Started
Appointment Started
{
  "invoice_id": "413c2fbe-e3a9-4638-a9c6-1369c8eccaf5",
  "invoice_number": "4901",
  "appointment_group_id": "1832089f-d2bc-402e-a56f-249e70492e2a",
  "center_id": "9a895b3c-1994-42c0-bc61-efda4a6e2828",
  "appointments": [
    {
      "id": "01d2dbac-51ad-4a5c-a252-40eaf47dd3a0",
      "invoice_item_id": "40a64c18-ae1e-4c5d-913c-0072763acd09",
      "service_name": "Service with segments",
      "service_id": "0e76466a-c514-447d-ac07-e04c0b86fdca",
      "start_time": "2022-02-21T18:30:00",
      "end_time": "2022-02-21T19:30:00",
      "serviceduration_in_miutes": 120,
      "has_add_ons": true,
      "is_add_on": false,
      "therapist_name": "RENU K",
      "TherapistId": "461ac926-2553-49f8-b9bd-0f7b6518daaa",
      "is_recurring": false,
      "appointment_type": 2,
      "therapist_request_type": 4,
      "room_name": "",
      "equipment_name": "",
      "room_id": "",
      "equipment_id: "",
      "appointment_progress": 1
    }
  ]
}


Updated over 2 years ago

Appointment Events
Appointment Completed
Did this page help you?
Yes
No
TABLE OF CONTENTS
Sample Response Code – Appointment Started