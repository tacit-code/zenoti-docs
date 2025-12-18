# Authentication

**Source:** https://docs.zenoti.com/reference/register-a-guest-to-a-workshop

**Endpoint:** `/v1/workshops/{workshop_id}/registrations`

---

## Description

Purpose: Use this API to register a guest to a workshop.

## , along with the body params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `workshop_id` | string | - | - |
| `track_id` | string | - | - |
| `guest_id` | string | - | - |
| `center_id` | string | - | - |

## Error occurs when the body params are not passed.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `workshop_id` | string | - | - |
| `track_id` | string | - | - |

## Path Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Body Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## No body params are passed

## Invalid workshop_id is passed in the path params

## - No body params are passed

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `200` | string | - | - |
| `400 - No body params are passed` | string | - | - |
| `400` | string | - | - |
| `400` | string | - | - |
| `400` | string | - | - |
| `400 - Registering a guest who is already enrolled` | string | - | - |
| `400` | string | - | - |
| `400` | string | - | - |

## - Invalid workshop id is passed in the path params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `200` | string | - | - |
| `400 - No body params are passed` | string | - | - |
| `400` | string | - | - |
| `400` | string | - | - |
| `400` | string | - | - |
| `400 - Registering a guest who is already enrolled` | string | - | - |
| `400` | string | - | - |
| `400` | string | - | - |

## Code Examples

### Python

```python
1
import requests
2
​
3
url = "https://api.zenoti.com/v1/workshops/workshop_id/registrations"
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

