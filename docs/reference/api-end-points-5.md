# Authentication

**Source:** https://docs.zenoti.com/reference/api-end-points-5

**Endpoint:** `/v1/opportunities`

---

## Description

Supply the opportunity object in the request body and this API will create an opportunity with given details.  Note: 'type' parameter is required to use Sales Stage Rules. Steps to create/edit Sales Stage Rules - Opportunities-> Sales Stage Rules.

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
url = "https://api.zenoti.com/v1/opportunities"
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
response = requests.post(url, headers=headers)
11
​
12
print(response.text)
```

