# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-consumption-details-of-products-for-a-center

**Endpoint:** `/v1/inventory/stock_movement`

---

## Description

This API retrieves the consumption details of all products for the specified center.

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
url = "https://api.zenoti.com/v1/inventory/stock_movement?report_type=1"
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

