# Authentication

**Source:** https://docs.zenoti.com/reference/remove-the-blockout-time-of-an-employee

**Endpoint:** `/v1/employees/{employee_id}/blockouttimes/{block_out_time_id}?mode=0&center_id={center_id}`

---

## Description

Permanently deletes a blockout time whose unique identifier is supplied as {block_out_time_id} and the unique id of the therapist as {employee_id}. It cannot be undone.

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
url = "https://api.zenoti.com/v1/employees/employee_id/blockouttimes/block_out_time_id?mode=0&center_id=center_id"
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
response = requests.delete(url, headers=headers)
11
​
12
print(response.text)
```

