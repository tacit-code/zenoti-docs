# Authentication

**Source:** https://docs.zenoti.com/reference/update-employee-of-the-center-with-given-catalog-details

**Endpoint:** `/v1/employees/{employee_id}`

---

## Description

This API updates the existing employee profile with additional parameters for taking catalog information. If the catalog details are provided then the same will be updated and other values are set to default. If the sub-object catalog details are not passed in the request body, the default values will be set for catalog details ('ShowInCatalog' are set to false and ‘DisplayName' and 'Description’ would be set to empty)..

## Optionally, you can specify updated information for any of the request body parameters.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `employee_id` | string | - | - |

## Request Body Parameters

## Path Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

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
url = "https://api.zenoti.com/v1/employees/employee_id"
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
response = requests.put(url, headers=headers)
12
​
13
print(response.text)
```

