# Authentication

**Source:** https://docs.zenoti.com/reference/fetch-a-list-of-booked-users-of-a-workshop-event

**Endpoint:** `/v1/workshops/{workshop_id}/registrations`

---

## Description

Purpose: Use this API to fetch a list of all the booked users of a particular workshop event.

## as query params.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `workshop_id` | string | - | - |
| `center_id` | string | - | - |
| `session_id` | string | - | - |

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
url = "https://api.zenoti.com/v1/workshops/workshop_id/registrations?page=1"
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

