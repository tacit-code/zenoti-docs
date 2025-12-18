# Authentication

**Source:** https://docs.zenoti.com/reference/unfreeze-the-membership-of-a-guest

**Endpoint:** `/v1/guests/{guest_id}/memberships/{user_membership_id}/unfreeze`

---

## Description

This API helps you to reactivate the membership of a guest.

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
url = "https://api.zenoti.com/v1/guests/guest_id/memberships/user_membership_id/unfreeze"
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

