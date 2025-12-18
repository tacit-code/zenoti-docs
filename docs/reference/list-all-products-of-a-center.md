# Authentication

**Source:** https://docs.zenoti.com/reference/list-all-products-of-a-center

**Endpoint:** `/v1/centers/{center_id}/products`

---

## Description

This API helps you to retrieve all the products that are active in the center on the specified date.

## query parameters if you have a large number of records to be displayed. By default,

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `center_id` | string | - | - |
| `center_id` | string | - | - |
| `page` | string | - | - |
| `size` | string | - | - |
| `page` | string | - | - |
| `size` | string | - | - |
| `size` | string | - | - |

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
url = "https://api.zenoti.com/v1/centers/center_id/products?page=1&size=10"
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

