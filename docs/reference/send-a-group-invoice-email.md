# Authentication

**Source:** https://docs.zenoti.com/reference/send-a-group-invoice-email

**Endpoint:** `/v1/group_invoices/{group_invoice_id}/email`

---

## Description

This API helps you to send a group invoice email to a guest.

## Request Body Parameters

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
url = "https://api.zenoti.com/v1/group_invoices/group_invoice_id/email"
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

