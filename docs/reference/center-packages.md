# Authentication

**Source:** https://docs.zenoti.com/reference/center-packages

**Endpoint:** `/v1/centers/{center_id}/packages`

---

## Description

This API helps you to retrieve all the packages that are active in the center. You must specify the unique identifier of the center as center_id in the API request.You can also leverage the pagination feature by passing page and size query parameters if you have a large number of records to be displayed. By default, page is set as 1 and size is set as 10. size cannot be more than 100: which means that the maximum records per page cannot be more than 100.

## query parameters if you have a large number of records to be displayed. By default,

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `center_id` | string | - | - |
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
url = "https://api.zenoti.com/v1/centers/center_id/packages?page=1&size=10&search_text=null&is_active=false&PackageType=null&series_package_type=null&member_price=false&guest_id=null&is_giftcard_enabled=false"
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

