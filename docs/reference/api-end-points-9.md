# Authentication

**Source:** https://docs.zenoti.com/reference/api-end-points-9

**Endpoint:** `/v1/vendors?page={page}&size={size}`

---

## Description

This API retrieves the list of all vendors for an organization.

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
url = "https://api.zenoti.com/v1/vendors?page=page&size=size"
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

