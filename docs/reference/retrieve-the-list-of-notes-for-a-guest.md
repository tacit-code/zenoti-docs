# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-list-of-notes-for-a-guest

**Endpoint:** `/v1/guests/{guest_id}/notes?view_private={view_private}&view_only_profile_alerts={view_only_profile_alerts}`

---

## Description

This API will help you to retrieve the notes created for the specified guest.

## query parameters if you have a large number of records to be displayed. By default,

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `guest_id` | string | - | - |
| `page` | string | - | - |
| `size` | string | - | - |
| `page` | string | - | - |
| `size` | string | - | - |
| `size` | string | - | - |

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
url = "https://api.zenoti.com/v1/guests/d6cfc4ed-f7b6-454a-a8cd-36a67a324e57/notes?view_private=view_private&view_only_profile_alerts=view_only_profile_alerts&noteType=-1&page=1&size=10"
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

