# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-loyalty-points-of-a-guest-earnedredeemed

**Endpoint:** `/v1/guests/{guestid}/points/{type}`

---

## Description

Purpose: Use this API to retrieve the details of loyalty points that are either earned or redeemed by the guest.

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
url = "https://api.zenoti.com/v1/guests/guestid/points/0"
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

