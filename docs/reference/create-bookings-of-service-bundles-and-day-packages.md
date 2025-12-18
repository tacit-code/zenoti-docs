# Authentication

**Source:** https://docs.zenoti.com/reference/create-bookings-of-service-bundles-and-day-packages

**Endpoint:** `/v1/bookings`

---

## Description

This API creates bookings of service bundles and day packages and also supports couple bookings.

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
url = "https://api.zenoti.com/api_url/v1/bookings"
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
response = requests.post(url, headers=headers)
11
​
12
print(response.text)
```

