# Authentication

**Source:** https://docs.zenoti.com/reference/changecancel-auto-renewal-of-guest-membership

**Endpoint:** `/v1/guests/{guest_id}/memberships/{user_membership_id}/renewal?guest_id&user_membership_id`

---

## Description

This API allows you to change or cancel the membership renewal of a guest.

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
url = "https://api.zenoti.com/v1/guests/guest_id/memberships/user_membership_id/renewal?guest_id=&user_membership_id="
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

