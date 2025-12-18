# Authentication

**Source:** https://docs.zenoti.com/reference/add-a-guest-pass-user

**Endpoint:** `/v1/guests/{user_id}/guestpass`

---

## Description

Purpose: Use this API to add a new Guest Pass user.
You must specify user_id and the body parameters as mentioned in the BODY PARAMS section.

## and the body parameters as mentioned in the BODY PARAMS section.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | - | - |

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
url = "https://api.zenoti.com/v1/guests/user_id/guestpass"
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

