# Authentication

**Source:** https://docs.zenoti.com/reference/booking-deleted

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
Booking Deleted
Sample Response Object – Booking Deleted
Booking Deleted
{
  "id": "6239c247a961750e01dda052",
  "event_id": "6239c247a961750e01dda051",
  "event_schema": "v1",
  "event_resource": "Class",
  "event_type": "Class.Booking.Deleted",
  "event_timestamp": "2022-03-22T12:34:15.3797492Z",
  "data": {
    "workshop_id": 11370,
    "track_id": -1,
    "class_id": 11370,
    "session_id": 89607,
    "add_to_all": null,
    "training_virtual_guests": null,
    "guest_id": "ef44e802-505c-4129-9744-0978c094c8f2",
    "center_id": "e1693623-bda5-4b3e-a2a7-611ea4f1f7ad",
    "waitlist": null,
    "booking_source": null,
    "registration_id": 119986,
    "group_invoice_id": null,
    "is_recurring": false,
    "recurrence_id": null,
    "recurrence_registration_ids": null,
    "guest_registration_ids": null
  }
}


Updated over 3 years ago

Booking Created
Booking Cancelled
Did this page help you?
Yes
No
TABLE OF CONTENTS
Sample Response Object – Booking Deleted