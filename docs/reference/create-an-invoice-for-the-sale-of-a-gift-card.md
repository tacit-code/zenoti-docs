# Authentication

**Source:** https://docs.zenoti.com/reference/create-an-invoice-for-the-sale-of-a-gift-card

**Endpoint:** `/v1/invoices/gift_cards`

---

## Description

This API helps you to create an invoice for the sale of a gift card without having to first create or select a gift card template.

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
url = "https://api.zenoti.com/v1/invoices/gift_cards"
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

