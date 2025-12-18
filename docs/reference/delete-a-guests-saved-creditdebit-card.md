# Authentication

**Source:** https://docs.zenoti.com/reference/delete-a-guests-saved-creditdebit-card

**Endpoint:** `/v1/guests/{guest_id}/accounts/{account_id}?center_id={center_id}`

---

## Description

If you have previously added credit/debit cards for the specified guest, this API helps you to delete the saved cards/active payment accounts of the guest.

## Path Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

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
url = "https://api.zenoti.com/v1/guests/guest_id/accounts/account_id?center_id=center_id"
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

