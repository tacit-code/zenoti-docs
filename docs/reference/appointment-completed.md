# Authentication

**Source:** https://docs.zenoti.com/reference/appointment-completed

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
Appointment Completed
Sample Response Object – Appointment Completed
Appointment Completed
{
  "invoice_id": "095b1101-2904-4bc2-9de4-043591fdfb8e",
  "invoice_number": "4902",
  "appointment_group_id": "6b675eff-35c9-4c40-8688-e4746a71fa98",
  "center_id": "9a895b3c-1994-42c0-bc61-efda4a6e2828",
  "appointments": [
    {
      "id": "e4895bb9-2ef5-4fb2-9cbe-318e07d251c7",
      "invoice_item_id": "39062a9e-4db7-4686-8c2a-22ea8adf1850",
      "service_name": "1 Service",
      "service_id": "4da307fb-0798-4b12-b34a-12be6903ef20",
      "start_time": "2022-02-25T06:00:00",
      "end_time": "2022-02-25T07:00:00",
      "serviceduration_in_miutes": 60,
      "has_add_ons": true,
      "is_add_on": false,
      "therapist_name": "Pavan K",
      "TherapistId": "40bed28f-6f27-4fd1-a65b-05e80a26b96a",
      "is_recurring": false,
      "appointment_type": 2,
      "therapist_request_type": 4,
      "room_name": "",
      "equipment_name": "",
      "room_id": "",
      "equipment_id: "",
      "appointment_progress": 2
    }
  ]
}


Updated over 2 years ago

Appointment Started
Appointment Feedback Event
Did this page help you?
Yes
No
TABLE OF CONTENTS
Sample Response Object – Appointment Completed