# Authentication

**Source:** https://docs.zenoti.com/reference/mark-an-appointment-as-confirm-or-undo-confirm

**Endpoint:** `/v1/invoices/{invoice_id}/confirm`

---

## Description

This API confirms a visit or is used to undo a confirmed visit.

## Query Params

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
url = "https://api.zenoti.com/v1/invoices/invoice_id/confirm?undo_confirm=false"
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
response = requests.put(url, headers=headers)
12
​
13
print(response.text)
```

