# Authentication

**Source:** https://docs.zenoti.com/reference/close-an-invoice

**Endpoint:** `/v1/invoices/{invoice_id}/close`

---

## Description

This API closes the specified invoice. You can only close an invoice after the total invoice amount has been paid in full (which means that the balance amount of the invoice is zero).

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
url = "https://api.zenoti.com/v1/invoices/invoice_id/close"
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

