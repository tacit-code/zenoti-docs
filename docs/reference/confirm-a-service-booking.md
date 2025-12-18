# Authentication

**Source:** https://docs.zenoti.com/reference/confirm-a-service-booking

**Endpoint:** `/v1/bookings/{booking_id}/slots/confirm`

---

## Description

This API helps you to confirm the required reserved service booking (booking_id).

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
url = "https://api.zenoti.com/v1/bookings/booking_id/slots/confirm"
4
​
5
headers = {
6
    "accept": "application/json",
7
    "content-type": "application/json",
8
    "Authorization": "apikey <your api key>"
9
}
10
​
11
response = requests.post(url, headers=headers)
12
​
13
print(response.text)
```

