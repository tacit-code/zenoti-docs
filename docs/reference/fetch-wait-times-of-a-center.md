# Authentication

**Source:** https://docs.zenoti.com/reference/fetch-wait-times-of-a-center

**Endpoint:** `/v1/queue/center_wait_times`

---

## Description

Purpose: The purpose of this API is to retrieve wait times for a list of centers or for centers in an area as per the Geolocation.

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
url = "https://api.zenoti.com/v1/queue/center_wait_times"
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

