# Authentication

**Source:** https://docs.zenoti.com/reference/delete-employee-medical-licenses

**Endpoint:** `/v1/employees/medical_licenses`

---

## Description

This API is designed to delete medical license details associated with an employee. It handles various types of medical licenses including License Numbers and DEA Numbers.

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
url = "https://api.zenoti.com/v1/employees/medical_licenses"
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

