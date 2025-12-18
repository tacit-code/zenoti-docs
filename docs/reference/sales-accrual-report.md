# Authentication

**Source:** https://docs.zenoti.com/reference/sales-accrual-report

**Endpoint:** `/v1/reports/sales/accrual_basis/flat_file`

---

## Description

The purpose of this API is to get the sales made by a center (on any particular day or over a time period) if the business follows accrual-based accounting.

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
url = "https://api.zenoti.com/v1/reports/sales/accrual_basis/flat_file"
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

