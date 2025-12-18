# Authentication

**Source:** https://docs.zenoti.com/reference/cancel-a-booking-registration

**Endpoint:** `/v1/Appointments/Sessions/{session_id}`

---

## Description

This API helps you to cancel the registration of a class session booking.

## Path Params

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
url = "https://api.zenoti.com/v1/Appointments/Sessions/session_id"
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
response = requests.delete(url, headers=headers)
11
​
12
print(response.text)
```

