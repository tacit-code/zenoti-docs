# service-booking-apis

**Source:** https://docs.zenoti.com/docs/service-booking-apis

---

### API workflow

### Take the following steps for booking a service:

Services include all the activities done for a guest by the service providers. These can range from massages to simple haircuts. In Zenoti, you can book services in Appointment Book, which allows you to schedule and manage your day's appointments.

The service booking APIs allow you to send the service booking data to your application. You can use this data to either monitor appointment bookings or manage your appointments in the ZMA (Zenoti Mobile Application).

Here's a video on how a service booking is done in the Zenoti web app:

Make sure the following things are in order before you proceed with the service booking APIs.

The Service Booking APIs allow you to search for a guest, add a service to the guest, and then book an appointment for the guest.

Updated about 3 years ago

- Services: Ensure you've created services for your center.
Note: Only Administrator or Owner role permission allows you to create the services at the organization level.
- Employee Schedules: Ensure all of your employee schedules are created.
Note: At least a single employee should be available and checked in for booking an appointment.
- Center Hours: Ensure you've configured your center's working hours.
- Block out Times: Ensure employee block-out times are configured, so as to allow them to take personal or other breaks.
- Payment Processor: Ensure you have an active payment processor. This will allow you to collect payments.

- Create a Booking
- Reserve a slot for booking
- Confirm the booking
- Collect payment for the invoice.

