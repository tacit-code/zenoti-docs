# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-a-service-of-a-center

**Endpoint:** `/v1/Centers/{center_id}/services/{service_id}`

---

## Description

This API helps you to retrieve the details of a specific service at the required center.

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
url = "https://api.zenoti.com/v1/Centers/center_id/services/service_id"
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

