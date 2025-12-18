# Authentication

**Source:** https://docs.zenoti.com/reference/list-all-therapists-of-a-center

**Endpoint:** `/v1/centers/{center_id}/therapists`

---

## Description

This API helps you to retrieve all the therapists that are active in the center on the specified date. You must specify the unique identifier of the center as center_id in the API request.

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
url = "https://api.zenoti.com/v1/centers/center_id/therapists"
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

