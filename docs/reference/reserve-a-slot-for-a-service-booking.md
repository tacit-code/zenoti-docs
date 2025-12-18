# Authentication

**Source:** https://docs.zenoti.com/reference/reserve-a-slot-for-a-service-booking

**Endpoint:** `/v1/bookings/{booking_id}/slots/reserve`

---

## Description

This API helps you to reserve a slot for the specified service booking (booking_id).You can also use this API to reserve a slot for the required group service booking (booking_id).You can choose a specific therapist or a therapist based on a certain gender while creating a service booking; after which, a unique 32-digit booking_id is generated.You must then specify the generated booking_id in the API request. You can also provide appropriate details for the slot_time parameter in the API request body to reserve a slot for the service booking.After you have reserved a slot for the service booking, you can then proceed to confirm the service booking.This API also allows guests to reserve appointments for family members. Provided, there is a relationship defined in Zenoti and an appointment reservation can only be done by the host.   Note: Invoice id is not generated in this step by default, It is generated only when you confirm a reservation with confirm a service booking API call. you can generate an temporary invoice in reserve slot API by using the create_invoice flag in the request body.

## Path Params

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
url = "https://api.zenoti.com/v1/bookings/booking_id/slots/reserve"
4
​
5
payload = {
6
    "slot_time": "2020-06-15T05:50:58",
7
    "create_invoice": False
8
}
9
headers = {
10
    "accept": "application/json",
11
    "content-type": "application/json",
12
    "Authorization": "apikey <your api key>"
13
}
14
​
15
response = requests.post(url, json=payload, headers=headers)
16
​
17
print(response.text)
```

