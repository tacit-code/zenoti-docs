# Authentication

**Source:** https://docs.zenoti.com/reference/security-roles

**Endpoint:** `/v1/employees/{employee_id}/security_roles`

---

## Description

The purpose of this API is to add a security role for an employee through the Roles tab of the Manage Employees page.

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
url = "https://api.zenoti.com/v1/employees/employee_id/security_roles"
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

