# Authentication

**Source:** https://docs.zenoti.com/reference/add-a-creditdebit-card-for-a-guest-service-booking-and-billing

**Method:** `POST`

**Endpoint:** `/v1/guests/{guest_id}/accounts`

---

## Description

The URL for this request expired after 30 days.

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
url = "https://api.zenoti.com/v1/guests/guest_id/accounts"
4
​
5
payload = { "source": "1" }
6
headers = {
7
    "accept": "application/json",
8
    "content-type": "application/json",
9
    "Authorization": "apikey <your api key>"
10
}
11
​
12
response = requests.post(url, json=payload, headers=headers)
13
​
14
print(response.text)
```

