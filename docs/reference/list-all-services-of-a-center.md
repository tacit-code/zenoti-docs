# Authentication

**Source:** https://docs.zenoti.com/reference/list-all-services-of-a-center

**Endpoint:** `/v1/Centers/{center_id}/services`

---

## Description

This API helps you to retrieve all the services that are active in a center.

## query parameters if you have a large number of records. By default,

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `center_id` | string | - | - |
| `expand` | string | - | - |
| `additional_info` | string | - | - |
| `catalog_info` | string | - | - |
| `category_id` | string | - | - |
| `variants_info` | string | - | - |
| `add_ons_info` | string | - | - |
| `image_paths` | string | - | - |
| `category_id` | string | - | - |
| `page` | string | - | - |
| `size` | string | - | - |
| `page` | string | - | - |
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
url = "https://api.zenoti.com/v1/Centers/center_id/services?page=1&size=10"
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

