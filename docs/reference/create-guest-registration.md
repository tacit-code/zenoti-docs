# Authentication

**Source:** https://docs.zenoti.com/reference/create-guest-registration

**Endpoint:** `/v1/classes/{class_id}/registrations`

---

## Description

Purpose: Use this API to register a guest for a class.

## as path params and mention the following in the body params - Check the body params section for more details.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `class_id` | string | - | - |

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
url = "https://api.zenoti.com/v1/classes/class_id/registrations"
4
​
5
payload = { "waitlist": True }
6
headers = {
7
    "accept": "application/json",
8
    "content-type": "application/json",
9
    "Authorization": "apikey <your api key>"
10
}
11
​
12
response = requests.post(url, json=payload, headers=headers)
13
​
14
print(response.text)
```

