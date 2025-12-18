# Authentication

**Source:** https://docs.zenoti.com/reference/api-end-points-2

**Endpoint:** `/v1/rooms/{room_id}/blockouttimes`

---

## Description

Use this API to create the blockout time of the specified room.

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
url = "https://api.zenoti.com/v1/rooms/room_id/blockouttimes"
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

