# Authentication

**Source:** https://docs.zenoti.com/reference/invoice-payments

**Endpoint:** `/v1/invoices/{invoice_id}/online_payments`

---

## Description

The URL for this request expired after 30 days.

## Path Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Body Params

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
url = "https://api.zenoti.com/v1/invoices/invoice_id/online_payments"
4
​
5
payload = {
6
    "tip_amount": 0,
7
    "source": 1
8
}
9
headers = {
10
    "content-type": "application/json",
11
    "Authorization": "apikey <your api key>"
12
}
13
​
14
response = requests.post(url, json=payload, headers=headers)
15
​
16
print(response.text)
```

