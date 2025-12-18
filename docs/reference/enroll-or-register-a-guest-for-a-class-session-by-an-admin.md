# Authentication

**Source:** https://docs.zenoti.com/reference/enroll-or-register-a-guest-for-a-class-session-by-an-admin

---

## Description

This API helps you to enroll or register a guest for a class session by an Admin.

## Request Body Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `SessionId` | string | - | - |
| `GuestId` | string | - | - |
| `BookingSrc` | string | - | - |

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
url = "https://api.zenoti.com/api/Appointments/Admin/Sessions?BookingSrc="
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

