# Authentication

**Source:** https://docs.zenoti.com/reference/freeze-the-membership-of-a-guest

**Endpoint:** `/v1/guests/{guest_id}/memberships/{user_membership_id}/freeze`

---

## Description

This API helps you to freeze the membership of a guest.

## Request Body Parameters

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
url = "https://api.zenoti.com/v1/guests/guest_id/memberships/user_membership_id/freeze"
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

