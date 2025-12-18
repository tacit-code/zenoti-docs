# Authentication

**Source:** https://docs.zenoti.com/reference/queue-apis

**Endpoint:** `/v1/queue/available_times`

---

## Description

Purpose: The purpose of this API is to retrieve the wait times of available stylists for a selected service in a center.

## Query Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Body Params

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
url = "https://api.zenoti.com/v1/queue/available_times?availability_by_time_slots=false&skip_catalog_validation=false&skip_kiosk_validation=false"
4
​
5
headers = {
6
    "accept": "application/json",
7
    "content-type": "application/json",
8
    "Authorization": "apikey <your api key>"
9
}
10
​
11
response = requests.post(url, headers=headers)
12
​
13
print(response.text)
```

