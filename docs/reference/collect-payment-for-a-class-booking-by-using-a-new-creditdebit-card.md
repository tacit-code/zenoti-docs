# Authentication

**Source:** https://docs.zenoti.com/reference/collect-payment-for-a-class-booking-by-using-a-new-creditdebit-card

---

## Description

This API helps you to save the new credit/debit card details of the guest and then collect payment for the class booking.

## Request Body Parameters

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
url = "https://api.zenoti.com/Catalog/Payments/Invoice/IntializePayment"
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

