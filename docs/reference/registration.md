# Authentication

**Source:** https://docs.zenoti.com/reference/registration

**Endpoint:** `/v1/classes/{class_id}/registrations?session_id={session_id}&center_id={center_id}&expand=session&expand=status_count&page=1&size=10`

---

## Description

This API helps you to retrieve a list of registrations for the class sessions.

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
url = "https://api.zenoti.com/v1/classes/class_id/registrations?page=1&size=10&session_id=session_id&center_id=center_id&expand=session&expand=status_count"
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

