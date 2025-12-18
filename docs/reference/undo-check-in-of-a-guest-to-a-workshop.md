# Authentication

**Source:** https://docs.zenoti.com/reference/undo-check-in-of-a-guest-to-a-workshop

**Endpoint:** `/v1/workshops/{workshop_id}/registrations/{registration_id}/undo_sign_in`

---

## Description

Use this API to undo the check-in of guests to a workshop.

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
url = "https://api.zenoti.com/v1/workshops/workshop_id/registrations/registration_id/undo_sign_in"
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

