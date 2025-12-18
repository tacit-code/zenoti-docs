# Authentication

**Source:** https://docs.zenoti.com/reference/package-invoices

**Endpoint:** `/v1/invoices/{invoice_id}/redemptions/packages`

---

## Description

This API allows you to redeem the regular Series Packages present in an invoice.

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
url = "https://api.zenoti.com/v1/invoices/invoice_id/redemptions/packages"
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

