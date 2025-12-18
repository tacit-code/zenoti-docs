# Authentication

**Source:** https://docs.zenoti.com/reference/guest-membership-created

---

## Description

Updated almost 2 years ago

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
Guest Membership Created
Sample Response Object – Guest Membership Created
Guest Membership Created
{
  "id": "658406afba62cd22dd23b663",
  "event_id": "658406afba62cd22dd23b662",
  "event_schema": "v1",
  "event_resource": null,
  "event_type": "Guest.Membership.Created",
  "event_timestamp": "2023-12-21T09:34:39.8025506Z",
  "data": {
    "guest_id": "5dbd3f94-9961-41eb-a7b0-480a8c49db4f",
    "payments": {
      "payment_type": 0,
      "duration": 0,
      "duration_type": 0,
      "default_payment_info": null
    },
    "pending_waive_collections": 0,
    "next_collection_date": null,
    "grace_period_date": null,
    "grace_period_days": 0,
    "recurrence_status": -1,
    "sold_by": {
      "id": null,
      "name": null
    },
    "payment_history": [],
    "has_digital_form": false,
    "user_membership_id": "c602e0d1-f9d2-4f37-809e-ceb882e59af4",
    "group_user_membership_id": "f86e948e-db35-4e33-9f39-4fe6cd4ed409",
    "status": 1,
    "is_refunded": false,
    "invoice": {
      "allow_other_centers_for_action_on_invoices": false,
      "item_id": "36b417b4-699c-4675-960e-7e33c9859a9d",
      "receipt_no": "BTSR522",
      "status": 4,
      "id": "f86e948e-db35-4e33-9f39-4fe6cd4ed409",
      "no": "BTS1325"
    },
    "membership": {
      "code": "T",
      "OTP_required": false,
      "T&C": null,
      "add_on_members_count": 0,
      "redemption_post_expiry_settings": {
        "can_select_specific_post_expiry_setting": false,
        "redeem_post_expiry": true,
        "grace_period_days": null
      },
      "guestpass_total": 0,
      "guestpass_balance": 0,
      "lock_cycles": 0,
      "restrict_cross_center_redemption": false,
      "type": 1,
      "freeze_fee_reason_enabled": false,
      "freeze_fee": null,
      "is_dicount_only_membership": null,
      "id": "365725fe-9a7b-4fd1-8990-cc33108bbb83",
      "name": "Test"
    },
    "recurring_details": null,
    "purchase": {
      "price": {
        "currency_id": 0,
        "sales": 0,
        "tax": 0,
        "final": 0
      },
      "date": "2023-12-21T00:00:00"
    },
    "tc_acceptedon": null,
    "expiry_date": "2024-12-20T00:00:00",
    "member_code": null,
    "members": [
      {
        "id": "5dbd3f94-9961-41eb-a7b0-480a8c49db4f",
        "name": "amarbir j (Primary)"
      }
    ],
    "credit_balance": {
      "total": 33.33,
      "service": 33.33,
      "product": 0,
      "other": 0,
      "comments": null
    },
    "center": {
      "id": "b787e08d-f393-4a26-a332-6050c8848d2a",
      "name": "Bethesda",
      "location": {
        "address_1": null,
        "address_2": null,
        "city": null,
        "state": null,
        "country": null
      },
      "time_zone": {
        "id": 0,
        "name": null,
        "standard_name": null,
        "identifier_name": null,
        "abbreviation": null
      }
    },
    "service_balance": [
      {
        "service": {
          "sale_as_part_of_package_or_membership_only": null,
          "book_with_partial_balance": 1,
          "item_type": null,
          "id": "f6ef34d9-20f6-464a-b6cf-5eb58e044925",
          "name": "SkinFit - Level 2",
          "duration": 60,
          "has_segments": false
        },
        "total": 1,
        "balance": 1,
        "redeemable_balance": 0,
        "used": 0,
        "transfered": 0,
        "expired": 0,
        "frequncy": "Any",
        "last_usage_date": null,
        "accrued_on": null,
        "is_category": false,
        "exists_in_current_center": true,
   