# Authentication

**Source:** https://docs.zenoti.com/reference/redeem-the-loyalty-points-of-a-guest

**Endpoint:** `/v1/invoices/{InvoiceId}/payments/loyalty_points`

---

## Description

Use this API to redeem a guest’s applicable loyalty points while taking payment for an invoice.

## In addition, you can specify the necessary details for the body parameters.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `InvoiceId` | string | - | - |
| `expand` | string | - | - |

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
url = "https://api.zenoti.com/v1/invoices/InvoiceId/payments/loyalty_points"
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
response = requests.post(url, headers=headers)
11
​
12
print(response.text)
```

