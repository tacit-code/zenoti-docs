# Authentication

**Source:** https://docs.zenoti.com/reference/update-the-schedule-of-an-employee

**Method:** `GET`

**Endpoint:** `/v1/employees/{employee_id}/schedules`

---

## Description

This API helps you to add, edit, or delete the schedule of the specified employee for any one particular day at a time.

## Path Params

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
url = "https://api.zenoti.com/v1/employees/employee_id/schedules"
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

