# Authentication

**Source:** https://docs.zenoti.com/reference/report-to-fetch-the-class-details-of-an-organization

**Endpoint:** `/v1/reports/classes/attendance/flat_file?page=1&size=10`

---

## Description

Purpose: Use this API to fetch the class details of an organization.

## along with other params as mentioned in the BODY PARAMS section.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `center_ids` | string | - | - |
| `employee_ids` | string | - | - |

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
url = "https://api.zenoti.com/v1/reports/classes/attendance/flat_file?page=1&size=10"
4
​
5
payload = { "class_type": "1" }
6
headers = {
7
    "accept": "application/json",
8
    "content-type": "application/json",
9
    "Authorization": "apikey <your api key>"
10
}
11
​
12
response = requests.get(url, json=payload, headers=headers)
13
​
14
print(response.text)
```

