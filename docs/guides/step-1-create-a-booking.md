# step-1-create-a-booking

**Source:** https://docs.zenoti.com/docs/step-1-create-a-booking

---

## 🚧Important

Search for a guest by using the Search for a guest API.
Note: There are multiple ways to search for a guest in Zenoti.

Search for a service by using the List all services of a center API.

If the guest wants to book an appointment for a specific therapist, list all the therapists by using the List all therapists of a center API.

If the guest wants to book a service appointment that is to be performed in a specific room of the center, list all the rooms by using the List all rooms of a center API.
Note: In order to allow guests to book specific rooms, you must create a service level association for the room.

Create a booking for the guest by using the Create a service booking API.

Important

While creating a service booking via either your custom mobile application or web application, you can specify the booking source: either External-Webstore or External-CMA. Zenoti assigns separate icons for such bookings in Appointment Book and as filter options in several appointment-related reports. As a result, you can pinpoint the appointments that you booked via APIs and easily track them in places such as Appointment Book and appointment-related reports. To enable this feature, contact your Zenoti Customer Service Manager (CSM).

Updated over 3 years ago

- Search for a guest by using the Search for a guest API.
Note: There are multiple ways to search for a guest in Zenoti.
- Search for a service by using the List all services of a center API.
- If the guest wants to book an appointment for a specific therapist, list all the therapists by using the List all therapists of a center API.
- If the guest wants to book a service appointment that is to be performed in a specific room of the center, list all the rooms by using the List all rooms of a center API.
Note: In order to allow guests to book specific rooms, you must create a service level association for the room.
- Create a booking for the guest by using the Create a service booking API.

- To reschedule a booking, use the Reschedule a booking API.
- To cancel a booking, invoke the Cancel a booking API.
Note: Canceled or no-show appointments can be viewed from the View Canceled/No Shows option in the context menu.

