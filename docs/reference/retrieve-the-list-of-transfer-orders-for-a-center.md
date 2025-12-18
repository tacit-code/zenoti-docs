# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-list-of-transfer-orders-for-a-center

**Endpoint:** `/v1/inventory/transfer_orders?center_id={center_id}&start_date={start_date}&end_date={end_date}&show_delivery_details={show_delivery_details}&date_criteria={date_criteria}&status={status}`

---

## Description

This API retrieves the list of transfer orders for the specified center during the specified time period.

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
url = "https://api.zenoti.com/v1/inventory/transfer_orders?show_delivery_details=show_delivery_details&date_criteria=date_criteria&status=status&center_id=center_id&start_date=start_date&end_date=end_date"
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

