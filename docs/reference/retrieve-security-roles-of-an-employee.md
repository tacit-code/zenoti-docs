# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-security-roles-of-an-employee

**Endpoint:** `/v1/employees/{employee_id}/security_roles?view_id={view_id}&view_type={view_type}`

---

## Description

The purpose of this API is to list all the security roles of an employee at all levels of the organization.

## Path Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

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
url = "https://api.zenoti.com/v1/employees/employee_id/security_roles?view_type=view_type&view_id=view_id"
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

