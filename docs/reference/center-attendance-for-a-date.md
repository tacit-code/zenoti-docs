# Authentication

**Source:** https://docs.zenoti.com/reference/center-attendance-for-a-date

**Endpoint:** `/v1/centers/{center_id}/attendance?date={date}`

---

## Description

This API retrieves the attendance of all the employees at a center on the specified date.

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
url = "https://api.zenoti.com/v1/centers/center_id/attendance?date=date"
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

