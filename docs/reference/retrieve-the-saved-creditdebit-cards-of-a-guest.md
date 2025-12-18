# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-saved-creditdebit-cards-of-a-guest

**Method:** `GET`

**Endpoint:** `/v1/guests/{guest_id}/accounts?center_id={center_id}`

---

## Description

The URL for this request expired after 30 days.

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
url = "https://api.zenoti.com/v1/guests/guest_id/accounts?center_id=center_id"
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

