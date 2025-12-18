# Authentication

**Source:** https://docs.zenoti.com/reference/sample-events

---

## Description

This automation notifies your application whenever an invoice is closed in Zenoti.

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
Invoice Closed
Guest Events
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
Invoice Closed

This automation notifies your application whenever an invoice is closed in Zenoti.

Check the API documentation for a closed invoice.

Sample Response Object
Invoice Closed
{
  "id": "622b5b33a961750e01db6512",
  "event_id": "622b5b33a961750e01db6510",
  "event_schema": "v1",
  "event_resource": "Invoice",
  "event_type": "Invoice.Closed",
  "event_timestamp": "2022-03-11T14:22:43.3847049Z",
  "data": {
    "invoice": {
      "id": "7e4e1a62-5982-4b3c-b9ac-da0f122e7ae5",
      "invoice_number": "7448",
      "receipt_number": "R2650",
      "appointment_group_id": "6849df99-3160-4475-a344-0495d34853fb",
      "lock": true,
      "is_closed": true,
      "is_refund": false,
      "invoice_date": "2022-03-11T08:00:00",
      "center_id": "5528ee09-5321-4153-8ca7-31c78d757dcb",
      "total_price": {
        "currency_id": 0,
        "net_price": 488,
        "tax": 0,
        "rounding_adjustment": 0,
        "sum_total": 488
      },
      "guest": {
        "id": "464d1eea-e19a-4880-ae4c-c2973b395981",
        "first_name": "test",
        "last_name": "membership",
        "gender": 1,
        "code": "",
        "mobile_phone": "+91 9885117036"
        "guest_email": ""
      },
      "invoice_items": [
        {
          "invoice_item_id": "aee902a5-ee52-4d1a-b16e-ceff7b1c6ae7",
          "id": "f2032f7a-033a-4806-afe0-e7c1a927d125",
          "name": "45 minutes cardio vascular test",
          "type": 0,
          "code": "45m1",
          "price": {
            "currency_id": 148,
            "sales": 0,
            "tax": 0,
            "final": 0,
            "discount": 0
          },
          "quantity": 1,
          "sale_by_id": "62ba6081-329e-4135-9c90-e4bc8ee35772",
          "therapist_name": "Henry Peterson"
        },
        {
          "invoice_item_id": "14ad8aac-cedc-47b0-af9c-5f71d028a529",
          "id": "d1894a6a-81c1-416b-9a9d-a94c8753f96f",
          "name": "17product'",
          "type": 2,
          "code": "awdsfd",
          "price": {
            "currency_id": 148,
            "sales": 88,
            "tax": 0,
            "final": 88,
            "discount": 12
          },
          "quantity": 1,
          "sale_by_id": "62ba6081-329e-4135-9c90-e4bc8ee35772",
          "therapist_name": "Henry Peterson"
        },
        {
          "invoice_item_id": "a48d3728-742c-480b-bb72-4bc302ee29c6",
          "id": "07ca7206-14db-490a-87c7-a1fd22de3bd9",
          "name": "PD-134509",
          "type": 3,
          "code": "jhge",
          "price": {
            "currency_id": 148,
            "sales": 400,
            "tax": 0,
            "final": 400,
            "discount": 0
          },
          "quantity": 1,
          "sale_by_id": "62ba6081-329e-4135-9c90-e4bc8ee35772",
          "therapist_name": "Henry Peterson"
        }
      ],
      "appointments": [
        {
          "id": "044a689a-9e0f-47e6-82b7-93c6fbe0c845",
          "invoice_item_id": "aee902a5-ee52-4d1a-b16e-ceff7b1c6ae7",
          "service_name": "45 minutes cardio vascular test",
          "service_id": "f2032f7a-033a-4806-afe0-e7c1a927d125",
          "start_time": "2022-03-11T02:30:00",
          "end_time": "2022-03-11T05:45:00",
          "serviceduration_in_miutes": 195,
          "has_add_ons": true,
          "is_add_on": false,
          "therapist_name": "Henry Peterson",
          "TherapistId": "62ba6081-329e-4135-9c90-e4bc8ee35772",
          "is_recurring": false,
          "appointment_type": 2,
          "therapist_request_type": 3,
          "room_name": "Room3",
          "equipment_name": ""
        }
      ],
      "transactions": [
        {
  