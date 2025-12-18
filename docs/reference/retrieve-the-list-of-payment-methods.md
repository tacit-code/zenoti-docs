# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-list-of-payment-methods

---

## Description

This API helps you to retrieve the list of payment methods that have been configured at the specified center.

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
url = "https://api.zenoti.com/Catalog/Payments/ProcessorSettings?CenterId=CenterId&Source=Source"
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

