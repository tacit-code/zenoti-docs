# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-a-center

**Endpoint:** `/v1/Centers/{center_id}`

---

## Description

This API helps you to retrieve the details of a center. You must specify the unique identifier of the center as center_id.

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
url = "https://api.zenoti.com/v1/Centers/center_id"
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

