# Authentication

**Source:** https://docs.zenoti.com/reference/update-the-password-of-a-guest-using-otp

**Endpoint:** `/v1/guests/{guest_id}/password`

---

## Description

This API helps you to update a guest's password by using the one-time password (OTP) that was sent to the guest's registered email ID after resetting the password.

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
url = "https://api.zenoti.com/v1/guests/guest_id/password"
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
response = requests.put(url, headers=headers)
12
​
13
print(response.text)
```

