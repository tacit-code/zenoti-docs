# Authentication

**Source:** https://docs.zenoti.com/reference/delete-a-product-from-an-invoice

**Endpoint:** `/v1/invoices/{invoice_id}/invoiceitems/{invoice_item_id}`

---

## Description

Use this API to delete a product from an invoice.

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
url = "https://api.zenoti.com/v1/invoices/invoice_id/invoiceitems/invoice_item_id"
4
​
5
headers = {
6
    "accept": "application/json",
7
    "content-type": "application/json",
8
    "Authorization": "apikey <your api key>"
9
}
10
​
11
response = requests.delete(url, headers=headers)
12
​
13
print(response.text)
```

