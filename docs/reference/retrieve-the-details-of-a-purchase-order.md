# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-details-of-a-purchase-order

**Endpoint:** `/v1/inventory/purchase_orders/{order_id}`

---

## Description

This API retrieves the details of the specified purchase order.

## Path Params

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
url = "https://api.zenoti.com/v1/inventory/purchase_orders/order_id"
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

