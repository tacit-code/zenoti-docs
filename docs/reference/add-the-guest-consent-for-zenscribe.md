# Authentication

**Source:** https://docs.zenoti.com/reference/add-the-guest-consent-for-zenscribe

**Endpoint:** `/v1/zenscribe/consents`

---

## Description

This API adds the guest consent for owner ID.

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
url = "https://api.zenoti.com/v1/zenscribe/consents"
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

