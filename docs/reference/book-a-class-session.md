# Authentication

**Source:** https://docs.zenoti.com/reference/book-a-class-session

---

## Description

This API helps you to create a booking for the specified class session for a signed-in guest.

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
url = "https://api.zenoti.com/Appointments/Sessions?SessionId=session_id&BookingSource=booking_source"
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
response = requests.post(url, headers=headers)
11
​
12
print(response.text)
```

