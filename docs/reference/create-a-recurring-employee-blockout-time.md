# Authentication

**Source:** https://docs.zenoti.com/reference/create-a-recurring-employee-blockout-time

**Endpoint:** `/v1/employees/{employee_id}/blockouttimes?expand[]=ReccuringDetails`

---

## Description

Description
Recurring blockout time blocks the specified time for repetive days. To create a recurring blockout time supply the blockouttime request object to this api and api will create the blockout time for specific therapist. To create a recurring block out time supply the recurring blockout time object. Request and respones of both recurring and non recurring block out times are given in examples.

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
url = "https://api.zenoti.com/v1/employees/employee_id/blockouttimes?expand=ReccuringDetails"
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

