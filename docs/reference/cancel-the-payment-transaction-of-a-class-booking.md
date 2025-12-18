# Authentication

**Source:** https://docs.zenoti.com/reference/cancel-the-payment-transaction-of-a-class-booking

**Endpoint:** `/v1/Catalog/Invoices/{invoice_id}/Cancel`

---

## Description

This API helps you to cancel the payment transaction flow of your class booking.

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
url = "https://api.zenoti.com/v1/Catalog/Invoices/invoice_id/Cancel"
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

