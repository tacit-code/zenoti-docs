# Authentication

**Source:** https://docs.zenoti.com/reference/fetch-employee-audit-report

**Endpoint:** `/v1/reports/audit/employee_activities/flat_file`

---

## Description

This API gives the audit report of the activities of employees based on the filter.

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
url = "https://api.zenoti.com/v1/reports/audit/employee_activities/flat_file"
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

