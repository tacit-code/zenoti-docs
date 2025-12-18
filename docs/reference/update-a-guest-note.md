# Authentication

**Source:** https://docs.zenoti.com/reference/update-a-guest-note

**Endpoint:** `/v1/guests/{guest_id}/notes/{note_id}`

---

## Description

This API helps you to update the details of the specified guest note.

## Request Body Parameters

## Path Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

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
url = "https://api.zenoti.com/v1/guests/d6cfc4ed-f7b6-454a-a8cd-36a67a324e57/notes/d6cfc4ed-f7b6-454a-a8cd-36a67a324e57"
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
response = requests.put(url, headers=headers)
12
​
13
print(response.text)
```

