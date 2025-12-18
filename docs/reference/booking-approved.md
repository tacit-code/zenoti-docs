# Authentication

**Source:** https://docs.zenoti.com/reference/booking-approved

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
Booking Created
Booking Deleted
Booking Cancelled
Booking No Show
Booking Approved
Booking Rejected
Guest Membership Events
Appointment Events
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
Booking Approved
Sample Response Object – Booking Approved
Booking Approved
{
    "workshop_id": 5543,
    "track_id": 1098,
    "class_id": 4567,
    "session_id": 55467,
    "add_to_all": 0,
    "guest_id": "204ad224-8f5d-4996-90f1-7add19e30213",
    "center_id": "442af543-6b2c-7677-65t3-4dff40d43987",
    "waitlist": true,
    "booking_source": 0,
    "registration_id": 43987,
    "group_invoice_id": "C35C1C68-208A-4CDB-A01E-DC541BA9D3C1",
    "training_virtual_guests": [{
      "guest_id": "43FAE108-E5CB-4CE0-8A73-87995DBEEF87",
      "registration_id": 43986,
      "first_name": "test",
      "last_name": "lastname",
      "email": "test@email.com",
      "mobile_phone":{
        "country_code": 91,
        "number": 7653467398
      },
      "gender": 1
    }],
    "recurrence_id": 23456,
    "recurrence_registration_ids": [55467, 55468]
}


Updated over 3 years ago

Booking No Show
Booking Rejected
Did this page help you?
Yes
No
TABLE OF CONTENTS
Sample Response Object – Booking Approved