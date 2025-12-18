# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-all-blockout-times-of-a-room

**Endpoint:** `/v1/rooms/{room_id}/blockouttimes?center_id={center_id}&start_date={start_date}&end_date={end_date}&expand[]=ReccuringDetails`

---

## Description

Use this API to retrieve all blockout times of the specified room.

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
url = "https://api.zenoti.com/v1/rooms/room_id/blockouttimes?center_id=center_id&start_date=start_date&end_date=end_date&expand=ReccuringDetails"
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

