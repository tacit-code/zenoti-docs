# Authentication

**Source:** https://docs.zenoti.com/reference/create-a-recurring-room-blockout-time

**Endpoint:** `/v1/rooms/{room_id}/blockouttimes?expand[]=ReccuringDetails`

---

## Description

Recurring blockout time block the time of the room every day repeatedly. To block a time for the room on the appointment book you can actually create a block out time for that room on the Appointment book whose ID is passed as {{room_id}}.Supply the BlockOutTimeRequest object as a body and call this api to create a blockout time.

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
url = "https://api.zenoti.com/v1/rooms/room_id/blockouttimes?expand=ReccuringDetails"
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

