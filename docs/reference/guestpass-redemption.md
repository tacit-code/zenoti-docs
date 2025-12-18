# Authentication

**Source:** https://docs.zenoti.com/reference/guestpass-redemption

---

## Description

If a GuestPass is redeemed during registration either on Zenoti Web or through API, Guestpass.redeemed event is triggered.

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
Guest Membership Created
Guest Membership Freeze
Guest Membership Unfreeze
Guest Membership Cancelled
Guest Membership Reinstate
GuestPass Redemption
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
GuestPass Redemption

If a GuestPass is redeemed during registration either on Zenoti Web or through API, Guestpass.redeemed event is triggered.

Sample Response Object – GuestPass Redemption
JSON
 {
    "id":"52923CDB-EA9B-420E-B787-1B2B4CE993AB",
    "date": "2022-07-17T23:15:00",
    "guestpass_id": "c7bc8109-6403-42dd-92ab-9aa22d84bee5",
    "guest_id": "184772fc-58bf-4257-b932-8d91be2b5736",
    "session_id": 81285,
    "invoice_id": "1db1854b-1ae3-401b-8302-1ef84de90ca4",
    "user_membership_id": "95f3175a-044d-47f2-9328-128a137b2ded",
    "membership": {
      "id": "70019c0a-4347-4c3a-81b0-2a53b8704270",
      "name": "Cycling"
    },
    "is_category": true,
    "total": 55,
    "balance": 23,
    "used": 32,
    "transferred": 0,
    "expired": 0,
    "frequency": "Any"
}


Updated almost 3 years ago

Guest Membership Reinstate
Appointment Events
Did this page help you?
Yes
No
TABLE OF CONTENTS
Sample Response Object – GuestPass Redemption