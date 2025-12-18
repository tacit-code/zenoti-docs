# Authentication

**Source:** https://docs.zenoti.com/reference/update-the-blockout-time-of-a-room

**Endpoint:** `/v1/rooms/{room_id}/blockouttimes/{block_out_time_id}?expand[]=ReccuringDetails`

---

## Description

Use this API to update the blockout time of the specified room.

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
url = "https://api.zenoti.com/v1/rooms/room_id/blockouttimes/block_out_time_id?expand=ReccuringDetails"
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
response = requests.put(url, headers=headers)
11
​
12
print(response.text)
```

