# Authentication

**Source:** https://docs.zenoti.com/reference/get-group-invoice-details

**Endpoint:** `/v1/group_invoices/{group_invoice_id}`

---

## Description

This API provides details of group invoices.

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
url = "https://api.zenoti.com/v1/group_invoices/group_invoice_id"
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

