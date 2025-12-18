# Authentication

**Source:** https://docs.zenoti.com/reference/create-new-guests-using-referral-codes

**Endpoint:** `/v1/guests`

---

## Description

This API creates new guests using correct referral codes.

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
url = "https://api.zenoti.com/api_url/v1/guests"
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

