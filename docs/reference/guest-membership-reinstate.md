# Authentication

**Source:** https://docs.zenoti.com/reference/guest-membership-reinstate

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
Guest Membership Reinstate
Sample Response Object – Guest Membership Reinstate
Guest Membership Reinstate
{
	"user_membership_id": "01192853-a6b5-4ff4-b299-e36b9efe61ac",
	"group_user_membership_id": "122df2ee-e82b-4c57-8262-ea57a39b6185",	
	"payments": {		
		"payment_type": 0,		
		"duration": 3,		
		"duration_type": 1,		
		"default_payment_info": "Cash"	
	},	
	"pending_waive_collections": 0,	
	"next_collection_date": "2021-12-24T00:00:00",	
	"grace_period_date": "2021-12-20T00:00:00",	
	"grace_period_days": 5,	
	"recurrence_status": 3,	
	"has_digital_form": false,	
	"status": 1,	
	"is_refunded": false,	
	"invoice": {		
		"allow_other_centers_for_action_on_invoices": false,		
		"item_id": null,		
		"receipt_no": "RRR5909",		
		"status": 4,		
		"id": "122df2ee-e82b-4c57-8262-ea57a39b6185",		
		"no": "RR16364"	
	},	
	"membership": {		
		"code": "fvdxv53634",		
		"OTP_required": false,		
		"T&C": "asddd",		
		"redemption_post_expiry_settings": {			
			"can_select_specific_post_expiry_setting": false,			
			"redeem_post_expiry": false		
		},		
		"type": 1,		
		"id": "cad826ab-5079-4e84-a600-d54909f013f9",		
		"name": "10- Massages - mem"	
	},	
	"purchase": {		
		"price": {			
			"currency_id": 0,			
			"sales": 0,			
			"tax": 0,			
			"final": 1000		
		},		
		"date": "2021-12-13T00:00:00"	
	},	
	"expiry_date": "2023-03-30T20:00:00",	
	"member_code": "vvs356371",	
	"members": [{			
			"id": "557f207c-c3c0-46ae-9bea-3815d90f16c8",			
			"name": "rajamouli s (Primary)"		
		}	
	],	
	"credit_balance": {		
		"total": 0,		
		"service": 0,		
		"product": 0,		
		"other": 0,		
		"comments": null	
	},	
	"center": {		
		"id": "a11f578a-1b81-4de0-8834-915f79e5362b",		
		"name": "Khammam"	
	},	
	"service_balance": [{			
			"service": {				
				"sale_as_part_of_package_or_membership_only": null,				
				"book_with_partial_balance": 1,				
				"id": "517ff077-1210-4f17-ad9a-c386e2c701aa",				
				"name": "Massages",				
				"duration": 0,				
				"has_segments": false			
			},			
			"total": 10,			
			"balance": 10,			
			"used": 0,			
			"transfered": 0,			
			"expired": 0,			
			"frequncy": "Any",			
			"last_usage_date": null,			
			"is_category": true,			
			"exists_in_current_center": true,			
			"discount_details": {				
				"discount_type": 0,				
				"peak_discount": 0,				
				"offpeak_discount": 0,				
				"post_credit_peak_discount": 0,				
				"post_credit_offpeak_discount": 0			
			},			
			"price": null		
		}	
	],	
	"auto_renewal": {		
		"selected_option": {			
			"renew_status": true,			
			"is_expired": false,			
			"renew_membership_amount": 0,			
			"id": "5878a83d-b322-4d26-838b-d5f042006cfa",			
			"name": "10- Massages - mem"		
		}	
	}
}


Updated over 3 years ago

Guest Membership Cancelled
GuestPass Redemption
Did this page help you?
Yes
No
TABLE OF CONTENTS
Sample Response Object – Guest Membership Reinstate