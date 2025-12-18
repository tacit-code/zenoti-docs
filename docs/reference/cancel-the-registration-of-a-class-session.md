# Authentication

**Source:** https://docs.zenoti.com/reference/cancel-the-registration-of-a-class-session

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
url = "https://api.zenoti.com/api/Appointments/Admin/Sessions/registration_id"
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

