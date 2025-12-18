# Authentication

**Source:** https://docs.zenoti.com/reference/group-invoice

**Endpoint:** `/v1/group_invoices`

---

## Description

This API helps you to create a group invoice.

## Code Examples

### Python

```python
1
import requests
2
​
3
url = "https://api.zenoti.com/v1/group_invoices"
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

