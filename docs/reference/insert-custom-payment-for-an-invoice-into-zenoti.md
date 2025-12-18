# Authentication

**Source:** https://docs.zenoti.com/reference/insert-custom-payment-for-an-invoice-into-zenoti

**Endpoint:** `/v1/invoices/{invoice_id}/payment/custom`

---

## Description

This API inserts the details of a custom payment (which has been collected by using a third-party software) for an invoice into Zenoti.

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
url = "https://api.zenoti.com/v1/invoices/invoice_id/payment/custom"
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

