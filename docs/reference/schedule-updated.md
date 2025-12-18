# Authentication

**Source:** https://docs.zenoti.com/reference/schedule-updated

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
Schedule Created
Schedule Updated
Schedule Cancelled
Schedule Deleted
Classes Booking Events
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
Schedule Updated
Sample Response Object – Schedule Updated
Schedule Updated
{
  "id": "6239ada0a961750e01dd9cb9",
  "event_id": "6239ada0a961750e01dd9cb7",
  "event_schema": "v1",
  "event_resource": "Class",
  "event_type": "Class.Schedule.Updated",
  "event_timestamp": "2022-03-22T11:06:08.1767409Z",
  "data": {
    "sesion_id": 89604,
    "center_id": "e1693623-bda5-4b3e-a2a7-611ea4f1f7ad",
    "class_name": "abc camp",
    "start_time": "2022-03-21T15:15:00",
    "end_time": "2022-03-21T18:00:00",
    "duration_in_mins": 45,
    "instructor_details_list": null,
    "room_id": null,
    "capacity": 10,
    "web_capacity": 5,
    "show_in_catalog": 1,
    "is_free_session": false,
    "description": "",
    "html_description": "",
    "is_recurring": false,
    "recurrence_start_time": null,
    "recurrence_end_time": null,
    "recurrence_type": null,
    "frequency": null,
    "num_occurences": null,
    "weekdays": null,
    "override_conflict_check": false,
    "enforce_add_on_conflict": false,
    "class_type": 1,
    "code": null,
    "event_id": -1,
    "student_virtual_link": "",
    "instructor_virtual_link": "",
    "recurrence_id": null,
    "recurrence_session_ids": null
  }
}


Updated over 3 years ago

Schedule Created
Schedule Cancelled
Did this page help you?
Yes
No
TABLE OF CONTENTS
Sample Response Object – Schedule Updated