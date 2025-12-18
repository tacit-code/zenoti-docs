# Authentication

**Source:** https://docs.zenoti.com/reference/update-billing-address-from-the-guest-profile

**Endpoint:** `/v1/guests/{guest_id}/accounts/{account_id}/billing_address`

---

## Description

Purpose: Use this API to update the billing address of the guest from the guest profile while saving a new card.

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
url = "https://api.zenoti.com/v1/guests/guest_id/accounts/account_id/billing_address"
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

