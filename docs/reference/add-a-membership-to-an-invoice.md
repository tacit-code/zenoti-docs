# Authentication

**Source:** https://docs.zenoti.com/reference/add-a-membership-to-an-invoice

**Endpoint:** `/v1/invoices/{invoice_id}/memberships`

---

## Description

Supply the url parameter invoice_id, request body and this api will update the requested invoice by booking the memberships aand returns the invoice id as the response.

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
url = "https://api.zenoti.com/v1/invoices/invoice_id/memberships"
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

