# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-list-of-purchase-orders-for-a-center

**Endpoint:** `/v1/inventory/purchase_orders`

---

## Description

This API retrieves the list of purchase orders for the specified center during the specified time period.

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
url = "https://api.zenoti.com/v1/inventory/purchase_orders?center_id=%7Bcenter_id%7D&start_date=2022-11-11&end_date=2022-11-12&show_delivery_details=false&date_criteria=3&status=-1"
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

