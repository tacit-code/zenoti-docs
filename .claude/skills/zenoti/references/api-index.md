# Zenoti API Endpoint Index

Categorized index of all 311 API endpoints. Use this to find the right endpoint for your task.

## Authentication
- `generate-an-access-token.md` - Get OAuth token
- `refresh-an-access-token.md` - Refresh expired token
- `revoke-an-existing-access-token.md` - Invalidate token
- `access-tokens.md` - Token overview

## Centers
- `list-all-centers.md` - Get all centers in organization
- `retrieve-a-center.md` - Get single center details
- `centers.md` - Centers overview
- `deactivate-or-disable-a-center.md` - Disable center
- `fetch-list-of-centers-based-on-parameters.md` - Filter centers

## Guests
- `create-a-guest.md` - Create new guest profile
- `search-for-a-guest.md` - Find guest by criteria
- `retrieve-guest-details.md` - Get guest profile
- `update-a-guest.md` - Modify guest data
- `list-all-guests-of-a-center.md` - All guests at center
- `merge-guests.md` - Combine duplicate profiles
- `guest-password.md` - Password management
- `reset-the-password-of-a-guest.md` - Password reset
- `update-the-password-of-a-guest-using-otp.md` - OTP password update
- `activate-guest-email.md` - Email activation

## Guest Notes & Forms
- `create-a-guest-note.md` - Add note to guest
- `retrieve-a-guest-note.md` - Get specific note
- `update-a-guest-note.md` - Modify note
- `delete-a-guest-note.md` - Remove note
- `retrieve-the-list-of-notes-for-a-guest.md` - All notes
- `create-a-guest-form.md` - Create intake form
- `retrieve-a-guest-form.md` - Get form data
- `update-a-guest-form.md` - Update form

## Service Booking
- `create-a-service-booking-copy.md` - Create booking
- `retrieve-available-slots-for-a-service-booking.md` - Get availability
- `reserve-a-slot-for-a-service-booking.md` - Hold slot (step 1)
- `confirm-a-service-booking.md` - Confirm booking (step 2)
- `cancel-a-service-booking.md` - Cancel booking
- `reschedule-a-service-booking.md` - Change booking time

## Appointments
- `list-all-appointments-of-a-guest.md` - Guest's appointments
- `retrieve-the-details-of-an-appointment.md` - Appointment details
- `retrieve-the-list-of-appointments-of-a-center.md` - Center appointments
- `mark-the-status-of-an-appointment-as-checked-in.md` - Check-in
- `undo-the-status-of-a-checked-in-appointment.md` - Undo check-in
- `mark-an-appointment-as-no-show.md` - No-show status
- `mark-an-appointment-as-confirm-or-undo-confirm.md` - Confirm status
- `update-appointment-progress-start-open-or-complete.md` - Progress status

## Services
- `list-all-services-of-a-center.md` - Center services
- `retrieve-a-service-of-a-center.md` - Service details
- `center-services.md` - Services overview
- `retrieve-therapist-pricing-and-price-scaling-for-a-service-at-a-center.md` - Service pricing

## Therapists & Employees
- `list-all-therapists-of-a-center.md` - Available therapists
- `list-all-employees-of-a-center.md` - All employees
- `employees.md` - Employee overview
- `retrieve-employee-details-with-payroll-information.md` - Employee details
- `add-employee-with-catalog-information.md` - Create employee
- `retrieve-the-schedules-of-employees-of-a-center.md` - Employee schedules
- `check-in-an-employee.md` - Employee check-in
- `check-out-an-employee.md` - Employee check-out

## Memberships
- `list-all-memberships-in-a-center.md` - Available memberships
- `list-all-memberships-of-a-guest.md` - Guest's memberships
- `create-an-invoice-for-memberships.md` - Start membership sale
- `add-a-membership-to-an-invoice.md` - Add to invoice
- `close-a-membership-sale-invoice.md` - Complete sale
- `cancel-the-membership-of-a-guest.md` - Cancel membership
- `freeze-the-membership-of-a-guest.md` - Pause membership
- `unfreeze-the-membership-of-a-guest.md` - Resume membership

## Packages
- `list-all-packages-of-a-center.md` - Available packages
- `list-the-series-packages-of-a-guest.md` - Guest's packages
- `create-an-invoice-for-the-sale-of-a-series-package.md` - Package sale
- `close-a-series-package-sale-invoice.md` - Complete package sale

## Gift Cards
- `list-all-gift-cards-of-a-guest.md` - Guest's gift cards
- `create-an-invoice-for-the-sale-of-a-gift-card.md` - Sell gift card
- `verify-the-balance-of-a-gift-card.md` - Check balance
- `send-a-gift-card-email-to-a-guest.md` - Email gift card

## Invoices & Payments
- `create-an-invoice-for-products.md` - Product invoice
- `retrieve-invoice-details.md` - Invoice details
- `close-an-invoice.md` - Complete invoice
- `invoice-payments.md` - Payment overview
- `collect-invoice-payment-by-using-a-guests-saved-creditdebit-card.md` - Saved card payment
- `collect-invoice-payment-by-using-a-guests-unsaved-creditdebit-card.md` - New card payment
- `collect-invoice-payment-by-redeeming-a-guests-gift-card.md` - Gift card payment
- `add-a-product-to-an-invoice.md` - Add product
- `delete-a-product-from-an-invoice.md` - Remove product

## Credit Cards
- `add-a-creditdebit-card-for-a-guest-service-booking-and-billing.md` - Save card
- `retrieve-the-saved-creditdebit-cards-of-a-guest.md` - List saved cards
- `delete-a-guests-saved-creditdebit-card.md` - Remove card

## Loyalty Points
- `retrieve-loyalty-points-of-a-guest.md` - Points balance
- `redeem-the-loyalty-points-of-a-guest.md` - Use points
- `verify-the-payable-loyalty-points-of-a-guest.md` - Check redeemable
- `retrieve-the-loyalty-points-history-of-a-guest.md` - Points history

## Classes & Workshops
- `classes-schedule.md` - Class schedules
- `book-a-class-session.md` - Book class
- `enroll-or-register-a-guest-for-a-class-session-by-an-admin.md` - Admin enrollment
- `cancel-a-guests-registration-to-a-class.md` - Cancel class registration
- `register-a-guest-to-a-workshop.md` - Workshop registration
- `cancel-a-guests-registration-to-a-workshop.md` - Cancel workshop

## Queue Management
- `queue-apis.md` - Queue overview
- `add-a-guest-or-group-of-guests-to-the-queue.md` - Add to queue
- `retrieve-the-list-of-all-appointments-in-queue-for-a-center.md` - View queue
- `fetch-wait-times-of-a-center.md` - Wait times

## Opportunities (Sales)
- `create-an-opportunity.md` - Create lead/opportunity
- `retrieve-an-opportunity.md` - Get opportunity
- `edit-an-opportunity.md` - Update opportunity
- `list-all-opportunities.md` - All opportunities
- `add-notes-to-an-opportunity.md` - Add notes

## Webhooks
- `webhook-events.md` - Webhook overview
- `booking-created.md` - Booking created event
- `booking-cancelled.md` - Booking cancelled event
- `guest-created.md` - Guest created event
- `guest-updated.md` - Guest updated event
- `invoice-closed-event.md` - Invoice closed event

## Reports
- `retrieve-the-collections-report-of-a-center.md` - Collections
- `retrieve-the-sales-report-of-a-center.md` - Sales report
- `fetch-collections-report.md` - Collections data
- `sales-accrual-report.md` - Sales accrual

## Rooms & Resources
- `list-all-rooms-of-a-center.md` - Available rooms
- `retrieve-a-room-of-a-center.md` - Room details
- `rooms.md` - Rooms overview
- `create-the-blockout-time-of-a-room.md` - Block room
- `remove-a-room-blockout-time.md` - Unblock room
