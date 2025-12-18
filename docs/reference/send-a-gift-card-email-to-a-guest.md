# Authentication

**Source:** https://docs.zenoti.com/reference/send-a-gift-card-email-to-a-guest

**Endpoint:** `/v1/invoices/{invoice_id}/send_giftcard_email`

---

## Description

If the invoice is closed and had complete payment invoke this api to Send giftcard mail to the guest.

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
url = "https://api.zenoti.com/v1/invoices/invoice_id/send_giftcard_email"
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

