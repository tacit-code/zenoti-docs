# Authentication

**Source:** https://docs.zenoti.com/reference/check-out-an-employee

**Endpoint:** `/v1/employees/{employee_id}/checkout`

---

## Description

This API helps you to check-out an employee.

## Request Body Parameters

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
url = "https://api.zenoti.com/v1/employees/employee_id/checkout"
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

