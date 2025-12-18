# Authentication

**Source:** https://docs.zenoti.com/reference/create-an-invoice-for-the-sale-of-a-series-package

---

## Description

This API helps you to create an invoice for the sale of a series package.

## Request Body Parameters

## Query Params

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
url = "https://api.zenoti.com/Catalog/SeriesPackages/CreateInvoice"
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

