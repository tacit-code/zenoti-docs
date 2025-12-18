# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-details-of-a-transfer-order

**Endpoint:** `/v1/inventory/transfer_orders/{order_id}`

---

## Description

This API retrieves the details of the specified transfer order.

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
url = "https://api.zenoti.com/v1/inventory/transfer_orders/order_id"
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

