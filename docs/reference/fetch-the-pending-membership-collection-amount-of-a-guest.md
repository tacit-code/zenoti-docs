# Authentication

**Source:** https://docs.zenoti.com/reference/fetch-the-pending-membership-collection-amount-of-a-guest

**Endpoint:** `/v1/guests/{guest_id}/memberships/{user_membership_id}/pending_dues`

---

## Description

This API helps you to fetch the pending membership collection amount that a guest needs to pay. This membership collection amount gets accumulated after a guest’s membership has been frozen on multiple occasions. Guests must pay that membership fee amount to reactivate their membership.

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
url = "https://api.zenoti.com/v1/guests/guest_id/memberships/user_membership_id/pending_dues"
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

