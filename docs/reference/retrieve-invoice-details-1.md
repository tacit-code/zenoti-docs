# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-invoice-details-1

**Endpoint:** `/v1/invoices/{invoice_id}`

---

## Description

This API fetches invoice details including GST sequence details. This invoice details API supports "expand" query parameter. The user has to pass "gst_parameters" to the "expand" query parameter.

## This API fetches invoice details including GST sequence details. This invoice details API supports "expand" query parameter. The user has to pass "gst_parameters" to the "expand" query parameter.

## Query Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Body Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Scenario 3: Get Invoice Details with query parameters "gst_parameters" and "dues_and_fees" and "Redemptions"

## Scenario 4: Get Invoice Details without query parameters "gst_parameters" and "dues_and_fees" and "Redemptions"

## - Scenario 3: Get Invoice Details with query parameters "gst parameters" and "dues and fees" and "Redemptions"

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `200` | string | - | - |
| `200` | string | - | - |
| `200` | string | - | - |
| `200` | string | - | - |

## - Scenario 4: Get Invoice Details without query parameters "gst parameters" and "dues and fees" and "Redemptions"

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `200` | string | - | - |
| `200` | string | - | - |
| `200` | string | - | - |
| `200` | string | - | - |

## Code Examples

### Python

```python
1
import requests
2
​
3
url = "https://api.zenoti.com/v1/invoices/invoice_id"
4
​
5
headers = {
6
    "accept": "application/json",
7
    "content-type": "application/json",
8
    "Authorization": "apikey <your api key>"
9
}
10
​
11
response = requests.get(url, headers=headers)
12
​
13
print(response.text)
```

