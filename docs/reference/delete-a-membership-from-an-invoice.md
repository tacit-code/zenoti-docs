# Authentication

**Source:** https://docs.zenoti.com/reference/delete-a-membership-from-an-invoice

**Endpoint:** `/v1/invoices/{invoice_id}/invoiceitems/{invoice_item_id}#`

---

## Description

Provide a unique identifier of the invoice as invoice_id and invoice_item_id of the membership you want to delete from the invoice and this API will delete that item from the invoice.

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
url = "https://api.zenoti.com/v1/invoices/invoice_id/invoiceitems/invoice_item_id#"
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

