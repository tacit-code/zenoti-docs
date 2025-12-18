# Authentication

**Source:** https://docs.zenoti.com/reference/guest-package-redemption

---

## Description

Updated over 3 years ago

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
Guest Package Events
Guest Package Creation
Guest Package Redemption
Guest Package Redemption Reversal
Guest Package Status Update
Guest Package Validity Update
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
Guest Package Redemption
Sample Response Code – Guest Package Redemption
Guest Package Redemption
{
    "user_package_id": "fe645486-7165-41de-8948-7f476c856824",
    "status": 1,
    "user_package_state": 2,
    "invoice": {
        "status": 0,
        "receipt_no": "0",
        "id": "4ed8572b-daaf-496a-8e36-aa27e8399917",
        "no": "RR16674"
    },
    "package": {
        "code": "15 min facial package",
        "is_OTP_required": false,
        "type": 0,
        "id": "e19e0f53-74d3-46b7-bc87-bef8fbc185c8",
        "name": "15 min facial package"
    },
    "purchase": {
        "price": {
            "currency_id": 0,
            "sales": 0,
            "tax": 0,
            "final": 110
        },
        "date": "2022-03-02T05:26:34"
    },
    "date": {
        "end_date_with_grace": "2022-04-26T00:00:00",
        "start": "2022-03-02T00:00:00",
        "end": "2022-04-01T00:00:00"
    },
    "schedule": {
        "completed_schedules": 1,
        "next_schedule_date": "2022-03-03T20:00:00"
    },
    "center": {
        "id": "a11f578a-1b81-4de0-8834-915f79e5362b",
        "name": "Khammam"
    },
    "is_refunded": false,
    "sale_invoice": {
        "id": null,
        "no": null
    },
    
    "lookup_package_user_id": null,
    "start_validity_at_first_redemption": false,
    "never_expires": false,
    "has_first_redemption": false,
    "expiration_days": 30,
    "service_redemptions":[
     {
    	"invoice": {
	        "status": 0,
	        "id": "4ed8572b-daaf-496a-8e36-aa27e8399917",
	        "no": "RR16674",
	        "item_id":"0cc3f6bd-680e-4953-bda6-9441565efb52"
        },
        "service": {
        	 "id":"4ed8572b-daaf-496a-8e36-aa27e8399917",
             "name" : "Aroma Body Massage"
        },
        "service_type_info": {
                "service_category_type": 1,
                "id": "977b2015-b764-452a-9562-a45a309ffcbe",
                "name": "Coloring"
        },
        "therapist": {
        	"id":"a11f578a-1b81-4de0-8834-915f79e5362b",
        	"name":"Raj Raj"
        },
        "usage_date":"2022-03-01 20:00:00.000",
        "center": {
	        "id": "a11f578a-1b81-4de0-8834-915f79e5362b",
	        "name": "Khammam"
        },
       }
      ],
     "product_redemptions":[
    	{
    	"invoice": {
	        "status": 0,
	        "id": "4ed8572b-daaf-496a-8e36-aa27e8399917",
	        "no": "RR16674",
	        "item_id":"0cc3f6bd-680e-4953-bda6-9441565efb52"
        },
        "product": {
        	 "id":"4ed8572b-daaf-496a-8e36-aa27e8399917",
             "name" : "Aroma Body Massage"
        },
        "product_type_info": {
                "product_category_type": 2,
                "id": "3fe77dd2-14b3-460c-ac0f-d0270408fe87",
                "name": "Apportion product 1"
        },
        "therapist": {
        	"id":"a11f578a-1b81-4de0-8834-915f79e5362b",
        	"name":"Raj Raj"
        },
        "usage_date":"2022-03-01 20:00:00.000",
        "center": {
	        "id": "a11f578a-1b81-4de0-8834-915f79e5362b",
	        "name": "Khammam"
        },
       }
      ]
}


Updated over 3 years ago

Guest Package Creation
Guest Package Redemption Reversal
Did this page help you?
Yes
No
TABLE OF CONTENTS
Sample Response Code – Guest Package Redemption