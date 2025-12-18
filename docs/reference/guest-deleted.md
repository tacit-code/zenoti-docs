# Authentication

**Source:** https://docs.zenoti.com/reference/guest-deleted

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
Guest Created
Guest Updated
Guest Deleted
Guest communication opted in
Guest communication opted out
Classes Schedule Events
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
Guest Deleted
Sample Response Object – Guest Deleted
Guest Deleted
{
  "id": "622b698ca961750e01db657e",
  "event_id": "622b698ca961750e01db657c",
  "event_schema": "v1",
  "event_resource": "Guest",
  "event_type": "Guest.Deleted",
  "event_timestamp": "2022-03-11T15:23:56.9931265Z",
  "data": {
    "id": "b9e61937-d5ce-46d5-be26-2659280d5eb9",
    "_id": 683768,
    "code": "1A347ABH",
    "center_id": "34aac717-e7df-4231-afc8-14420213957c",
    "center_name": "Chicago",
    "created_date": "2022-03-11T14:59:49",
    "personal_info": {
      "user_name": "",
      "first_name": "Joseph",
      "last_name": "Harrington",
      "middle_name": "",
      "email": "",
      "mobile_phone": null,
      "work_phone": null,
      "home_phone": null,
      "gender": 0,
      "date_of_birth": null,
      "is_minor": false,
      "nationality_id": 95,
      "anniversary_date": null,
      "lock_guest_custom_data": false,
      "pan": "",
      "dob_incomplete_year": ""
    },
    "address_info": {
      "address_1": "",
      "address_2": "",
      "city": "",
      "country_id": 225,
      "state_id": -1,
      "state_other": "",
      "zip_code": "29214"
    },
    "preferences": {
      "receive_transactional_email": true,
      "receive_transactional_sms": true,
      "receive_marketing_email": true,
      "receive_marketing_sms": true,
      "recieve_lp_stmt": true,
      "opt_in_for_loyalty_program": true,
      "transactional_sms_optin": 1,
      "transactional_email_optin": 1,
      "marketing_sms_optin": 1,
      "marketing_email_optin": 1,
      "transactional_whatsapp_optin": 6,
      "receive_transactional_whatsapp": false
    }
  }
}


Updated over 3 years ago

Guest Updated
Guest communication opted in
Did this page help you?
Yes
No
TABLE OF CONTENTS
Sample Response Object – Guest Deleted