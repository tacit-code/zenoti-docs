# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-list-of-all-appointments-in-queue-for-a-center

**Endpoint:** `/v1/queue?CenterId={center_id}`

---

## Description

Purpose: Use this API to list all the appointments in your queue.

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
url = "https://api.zenoti.com/v1/queue?CenterId=center_id"
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

