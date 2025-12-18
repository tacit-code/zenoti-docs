# Authentication

**Source:** https://docs.zenoti.com/reference/redeem-a-guests-guest-pass

**Endpoint:** `/v1/guests/{guest_id}/guestpass/{guestpass_id}/redeem`

---

## Description

Purpose: Use this API to redeem the benefits of the guest's Guest Pass membership.

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
url = "https://api.zenoti.com/v1/guests/guest_id/guestpass/guestpass_id/redeem"
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

