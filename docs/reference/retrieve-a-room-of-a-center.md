# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-a-room-of-a-center

**Endpoint:** `/v1/centers/{center_id}/rooms/{room_id}`

---

## Description

This API helps you to retrieve the details of a specific room at the required center.

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
url = "https://api.zenoti.com/v1/centers/center_id/rooms/room_id"
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

