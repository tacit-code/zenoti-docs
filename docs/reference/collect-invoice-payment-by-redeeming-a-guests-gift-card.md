# Authentication

**Source:** https://docs.zenoti.com/reference/collect-invoice-payment-by-redeeming-a-guests-gift-card

**Endpoint:** `/v1/invoices/{invoice_id}/payments/gift_card`

---

## Description

This API helps you to collect payment for the amount of an invoice by redeeming the balance of a guest’s gift card.

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
url = "https://api.zenoti.com/v1/invoices/invoice_id/payments/gift_card"
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

