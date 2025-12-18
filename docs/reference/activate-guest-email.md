# Authentication

**Source:** https://docs.zenoti.com/reference/activate-guest-email

**Endpoint:** `/v1/guests/{guest_id}/email_activate`

---

## Description

This API activates a guest's email address by marking it as valid in the system.

## Code Examples

### Python

```python
1
import requests
2
​
3
url = "https://api.zenoti.com/v1/guests/guest_id/email_activate"
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
response = requests.put(url, headers=headers)
11
​
12
print(response.text)
```

