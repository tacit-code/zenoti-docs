# Authentication

**Source:** https://docs.zenoti.com/reference/appointment-group-created

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
Appointment Group Created
Sample Response Object – Appointment Group Created
Appointment Group Created
{
  "id": "66a26696c7314f7815db6a1f",
  "event_id": "66a26696c7314f7815db6a1e",
  "event_schema": "v1",
  "event_resource": null,
  "event_type": "AppointmentGroup.Created",
  "event_timestamp": "2024-07-25T14:52:06.769417Z",
  "data": {
    "invoice_id": "e8cedcb5-58b7-42bf-8024-7184c877aa03",
    "invoice_number": "8086",
    "invoice_number_prefix": "BEL1",
    "utm_source": "facebook",
    "utm_medium": "online",
    "appointment_group_id": "883ce749-12a8-497b-bc50-2c3206c50e91",
    "organization_id": "edc06ff1-d9b4-4b93-80b6-908715a574c3",
    "center_id": "1aab4fd2-2ff3-4ede-bca2-74aa2ccb54b6",
    "center_Name": "Bellevue",
    "guest": {
      "id": "d08327d8-f928-4c37-8be3-87b93c90ac56",
      "first_name": "Abc",
      "last_name": "test",
      "email": "aa@swd.wed"
    },
    "appointments": [
      {
        "id": "ce5dd625-2bef-4b93-9418-a54bee1d36d3",
        "invoice_item_id": "7d05cb41-0a36-4966-90ad-56bde1c6e4a4",
        "service_name": "Laser Hair - Male",
        "service_id": "acedc3fc-38cf-48f9-ae5c-61b81649d841",
        "start_time": "2024-07-25T16:15:00",
        "end_time": "2024-07-25T17:15:00",
        "start_time_in_center": "2024-07-25T09:15:00",
        "end_time_in_center": "2024-07-25T10:15:00",
        "creation_date": "2024-07-25T14:52:06",
        "last_updated_on": "2024-07-25T14:52:06",
        "service_duration_in_minutes": 60,
        "has_add_ons": false,
        "is_add_on": false,
        "therapist_name": "DebashisTest TripathyTest",
        "therapist_id": "79ef653b-9dbf-40c4-b457-6fee1ca0eaf5",
        "is_recurring": false,
        "show_in_calendar": true,
        "appointment_type": 2,
        "therapist_request_type": 0,
        "room_id": "a35dbd63-fdc2-4dea-aeb0-eadb222796bb",
        "room_name": "Roomsacred Hours",
        "equipment_name": ""
      }
    ]
  }
}


Updated 10 months ago

Appointment Group Events
Appointment Group Status
Did this page help you?
Yes
No
TABLE OF CONTENTS
Sample Response Object – Appointment Group Created