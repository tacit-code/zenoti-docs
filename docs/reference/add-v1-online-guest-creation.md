# Authentication

**Source:** https://docs.zenoti.com/reference/add-v1-online-guest-creation

**Endpoint:** `/v1/guests/online_guests`

---

## Description

This API creates new online guests from custom webstores to support “Checkout as guest” flows. This is a dummy guest and is not retrievable on Zenoti POS.

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
url = "https://api.zenoti.com/v1/guests/online_guests"
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
response = requests.post(url, headers=headers)
12
​
13
print(response.text)
```

