# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-employee-details-with-payroll-information

**Endpoint:** `/v1/employees/{employee_id}`

---

## Description

The purpose of this API is to retrieve employee details with payroll information.

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
url = "https://api.zenoti.com/v1/employees/employee_id"
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

