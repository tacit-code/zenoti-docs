# Authentication

**Source:** https://docs.zenoti.com/reference/create-a-service-booking-copy

**Endpoint:** `/v1/bookings?is_double_booking_enabled={is_double_booking_enabled}`

---

## Description

This API helps you to create a service booking request for an appointment. To create a group service booking, you must specify in the API request body the required guest_id and appointment-related item details. After you add appointment details for multiple guests, this API automatically creates a group booking. For more information on these parameters and how to create a group booking, refer to the Request Body Details table and the Body section respectively.If you have a preference for a specific therapist for the service, you can specify the required therapist ID in the API request body. If you have a preference for a specific gender of therapist for the service, you can specify the required gender option in the API request body.After you use this API to create a service booking, a unique 32-digit booking_id is generated. You can then use this booking_id to retrieve available slots for the service booking, reserve a slot for the service booking, and then confirm the service booking to complete the appointment-booking process.This API also allows guests to create service bookings for other guests, provided there is a relationship defined in Zenoti, and the booking can only be done by the host.  The host_id parameter in the request object can also select the host for group bookings. This API now supports Zenoti growth features.

## Path Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Query Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Body Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Code Examples

### Python

```python
1
import requests
2
​
3
url = "https://api.zenoti.com/v1/bookings?is_double_booking_enabled=true (COPY)"
4
​
5
payload = { "is_only_catalog_employees": True }
6
headers = {
7
    "accept": "application/json",
8
    "content-type": "application/json",
9
    "Authorization": "apikey <your api key>"
10
}
11
​
12
response = requests.post(url, json=payload, headers=headers)
13
​
14
print(response.text)
```

