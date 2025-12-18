# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-list-of-all-products-associated-to-a-vendor

**Endpoint:** `/v1/vendors/{vendor_id}/products?page={page}&size={size}`

---

## Description

This API retrieves the list of all products associated to a vendor.

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
url = "https://api.zenoti.com/v1/vendors/vendor_id/products?page=page&size=size"
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

