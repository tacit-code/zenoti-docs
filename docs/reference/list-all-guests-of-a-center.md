# Authentication

**Source:** https://docs.zenoti.com/reference/list-all-guests-of-a-center

**Endpoint:** `/v1/guests?center_id={center_id}&last_updated={date}`

---

## Description

This API helps you to retrieve all guests of the specified center.

## query parameters if you have a large number of records to be displayed. By default,

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `center_id` | string | - | - |
| `page` | string | - | - |
| `size` | string | - | - |
| `page` | string | - | - |
| `size` | string | - | - |
| `size` | string | - | - |

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
url = "https://api.zenoti.com/v1/guests?page=1&size=10&center_id=center_id&last_updated=date"
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

