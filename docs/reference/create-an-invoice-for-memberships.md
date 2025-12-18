# Authentication

**Source:** https://docs.zenoti.com/reference/create-an-invoice-for-memberships

**Endpoint:** `/v1/invoices/memberships`

---

## Description

Supply the request body and this api will generate an invoice by booking the memberships aand returns the invoice id as the response.

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
url = "https://api.zenoti.com/v1/invoices/memberships"
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
response = requests.post(url, headers=headers)
12
​
13
print(response.text)
```

