# Authentication

**Source:** https://docs.zenoti.com/reference/send-an-email-to-a-guest

**Endpoint:** `/v1/invoices/{invoice_id}/email`

---

## Description

If the invoice is closed and has complete payment, invoke this api to e-mail to the guest.

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
url = "https://api.zenoti.com/v1/invoices/invoice_id/email"
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
response = requests.put(url, headers=headers)
11
​
12
print(response.text)
```

