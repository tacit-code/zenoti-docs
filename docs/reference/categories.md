# Authentication

**Source:** https://docs.zenoti.com/reference/categories

**Endpoint:** `/v1/centers/{center_id}/categories`

---

## Description

This API helps you to retrieve the list of categories that are active in a center.
You must specify the unique identifier of the location (center) in the API request as center_id.

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
url = "https://api.zenoti.com/v1/centers/center_id/categories?page=1&size=10&type=1"
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

