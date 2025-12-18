# Authentication

**Source:** https://docs.zenoti.com/reference/employee-created

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
Employee Events
Employee Deleted
Employee Created
Employee Updated
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
Employee Created
Sample Response Object – Employee Created
Employee Created
{
  "id": "62399306a961750e01dd998e",
  "event_id": "62399306a961750e01dd998d",
  "event_schema": "v1",
  "event_resource": "Employee",
  "event_type": "Employee.Created",
  "event_timestamp": "2022-03-22T09:12:38.7800898Z",
  "data": {
    "id": "ba06e416-a2c2-4324-a6ef-e328ff91bbc2",
    "code": "246",
    "center_id": "99d6833e-ceb9-4232-85c8-05fb78bd2519",
    "is_consultant": null,
    "created_by": "00000000-0000-0000-0000-000000000000",
    "personal_info": {
      "first_name": "George",
      "middle_name": "",
      "last_name": "Soderdam",
      "nick_name": "",
      "notification_name": "George Soderdam",
      "email": "George@abc.com",
      "mobile_phone": {
        "country_code": 1,
        "number": ""
      },
      "home_phone": {
        "country_code": 1,
        "number": ""
      },
      "work_phone": {
        "country_code": 1,
        "number": ""
      },
      "gender": -1,
      "birth_date": "0001-01-01T00:00:00",
      "anniversary_date": "0001-01-01T00:00:00"
    },
    "address": {
      "address_1": "",
      "address_2": "",
      "city": "",
      "country_id": 225,
      "state_id": 125,
      "zip_code": ""
    },
    "login_info": {
      "username": "george@abc.com"
    },
    "job_info": {
      "job_id": "aa165487-d5b0-4525-ab24-1579eb6fb9fe",
      "job_name": "BEAUTICIAN",
      "designation_id": null,
      "company_name": "KQA",
      "salary": 0,
      "hourly_rate": 0,
      "overtime_baseline_hours": 0,
      "overtime_type": 0,
      "overtime_multiplier": 1,
      "work_task_ids": null,
      "request_therapist_bonus": 0,
      "mandatory_break_period": 0,
      "is_elgible_for_additional_commision_bonus": false,
      "max_work_hours": 0,
      "target_revenue": 0,
      "vacation_days": 0,
      "special_leave_days": 0,
      "start_date": "2022-03-22T00:00:00",
      "end_date": "0001-01-01T00:00:00",
      "tenure_start_date": "0001-01-01T00:00:00",
      "pay_type": 0
    },
    "preference_info": {
      "culture_id": 54,
      "search_tags": "",
      "receive_marketing_emails": true,
      "receive_marketing_messages": true,
      "receive_transactional_emails": true,
      "receive_transactional_messages": true,
      "receive_daily_reports": false,
      "receive_register_closure_report": false,
      "waive_biometric_checkin": false,
      "access_manager_productivity_app": false,
      "is_mentor": false,
      "access_employee_productivity_app": false,
      "access_code": "",
      "keyword": "",
      "allow_analytics_access": 0,
      "allow_api_access": false,
      "text_field_1": "",
      "text_field_2": "",
      "additional_date_1": "0001-01-01T00:00:00",
      "additional_date_2": "0001-01-01T00:00:00",
      "send_confirmation_for_scheduled_appointments": true
    },
    "payroll_info": {
      "include_in_payroll": 1
    },
    "vanity_image_url": null,
    "roles": {
      "security_profile_id": "00000000-0000-0000-0000-000000000000"
    },
    "catalog_info": {
      "show_in_catalog": false,
      "display_name": "",
      "description": ""
    }
  }
}


Updated over 3 years ago

Employee Deleted
Employee Updated
Did this page help you?
Yes
No
TABLE OF CONTENTS
Sample Response Object – Employee Created