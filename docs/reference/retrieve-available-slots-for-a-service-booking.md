# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-available-slots-for-a-service-booking

**Endpoint:** `/v1/bookings/{booking_id}/slots`

---

## Description

This API helps you to retrieve available slots for the specified service booking (booking_id) on a given day. If no slots are available on that day, the API returns the next available slot on any other future day of the current week.

## Path Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Query Params

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
url = "https://api.zenoti.com/v1/bookings/booking_id/slots?check_future_day_availability=false"
4
​
5
headers = {
6
    "accept": "application/json",
7
    "Authorization": "apikey <your api key>"
8
}
9
​
10
response = requests.get(url, headers=headers)
11
​
12
print(response.text)
```

