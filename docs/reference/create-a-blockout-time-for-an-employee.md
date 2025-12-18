# Authentication

**Source:** https://docs.zenoti.com/reference/create-a-blockout-time-for-an-employee

**Endpoint:** `/v1/employees/{employee_id}/blockouttimes`

---

## Description

This API helps you to create a blockout time for the specified employee.

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
url = "https://api.zenoti.com/v1/employees/employee_id/blockouttimes"
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

