# Authentication

**Source:** https://docs.zenoti.com/reference/api-end-points-10

**Endpoint:** `/v1/inventory/stock?center_id={center_id}&inventory_date={inventory_date}&search_string={seach_string}&product_type={product_type}`

---

## Description

This API fetches the stock quantities of all products in the specified center.

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
url = "https://api.zenoti.com/v1/inventory/stock?search_string=seach_string&product_type=product_type&center_id=center_id&inventory_date=inventory_date"
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

