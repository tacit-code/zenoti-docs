# Authentication

**Source:** https://docs.zenoti.com/reference/create-a-gift-card-sale-invoice-after-using-a-gift-card-template

**Endpoint:** `/v1/invoices/giftcards`

---

## Description

You must specify appropriate details for the request body parameters, and this API generates an invoice by booking the gift cards and returns a unique invoice ID as the response.

## You must specify appropriate details for the request body parameters, and this API generates an invoice by booking the gift cards and returns a unique invoice ID as the response.

## Code Examples

### Python

```python
1
import requests
2
​
3
url = "https://api.zenoti.com/v1/invoices/giftcards"
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

