# Authentication

**Source:** https://docs.zenoti.com/reference/get-the-guest-consent-for-zenscribe

**Endpoint:** `/v1/zenscribe/consents`

---

## Description

This API fetches guest consent.

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
url = "https://api.zenoti.com/v1/zenscribe/consents"
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

