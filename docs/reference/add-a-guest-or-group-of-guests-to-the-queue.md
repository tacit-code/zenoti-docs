# Authentication

**Source:** https://docs.zenoti.com/reference/add-a-guest-or-group-of-guests-to-the-queue

**Endpoint:** `/v1/queue/bookings`

---

## Description

Purpose: The purpose of this API is to add a guest or a group of guests to the queue for a given center.

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
url = "https://api.zenoti.com/v1/queue/bookings"
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

