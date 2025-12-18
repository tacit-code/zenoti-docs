# Authentication

**Source:** https://docs.zenoti.com/reference/guest-membership-change-log

**Endpoint:** `/v1/guests/memberships/change_log?center_id={center_id}&guest_id={guest_id}&start_date={start_date}&end_date={end_date}&page=1&size=10`

---

## Description

This API helps you to retrieve the changes to the Guest's Membership, in the specified window.

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
url = "https://api.zenoti.com/v1/guests/memberships/change_log?page=1&size=10&center_id=center_id&guest_id=guest_id&start_date=start_date&end_date=end_date"
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

