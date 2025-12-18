# Authentication

**Source:** https://docs.zenoti.com/reference/check-aveda-birthday-gift-availability

**Endpoint:** `/v1/guests/{guest_id}/aveda/birthday_gift`

---

## Description

This API checks if a guest is eligible for an Aveda birthday gift. It validates whether the guest is an Aveda member and if a birthday gift offer code can be claimed.

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
url = "https://api.zenoti.com/v1/guests/guest_id/aveda/birthday_gift"
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

