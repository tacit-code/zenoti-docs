# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-details-of-all-the-members-of-a-center

**Endpoint:** `/v1/centers/{center_id}/members?status={status}&created_date={date}&last_updated_date={date}&page={page}&size={size}`

---

## Description

This API helps you to retrieve the list of memebers in the specified center.

## query parameters if you have a large number of records to be displayed. By default,

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `center_id` | string | - | - |
| `page` | string | - | - |
| `size` | string | - | - |
| `page` | string | - | - |
| `size` | string | - | - |
| `size` | string | - | - |

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
url = "https://api.zenoti.com/v1/centers/center_id/members?page=page&size=size&status=status&created_date=date&last_updated_date=date"
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

