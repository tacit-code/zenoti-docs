# Authentication

**Source:** https://docs.zenoti.com/reference/refresh-an-access-token

**Endpoint:** `/v1/tokens#`

---

## Description

Purpose: Use this API to refresh an expired access token. Since an access token is valid for 24 hours, you must use this API to generate a new access token.

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
url = "https://api.zenoti.com/v1/tokens#"
4
​
5
headers = {
6
    "accept": "text/plain",
7
    "content-type": "application/json"
8
}
9
​
10
response = requests.post(url, headers=headers)
11
​
12
print(response.text)
```

