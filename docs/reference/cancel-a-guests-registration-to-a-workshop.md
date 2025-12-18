# Authentication

**Source:** https://docs.zenoti.com/reference/cancel-a-guests-registration-to-a-workshop

**Endpoint:** `/v1/workshops/{workshop_id}/registrations/{registration_id}/cancel`

---

## Description

Purpose: The purpose of this API is to cancel the guest's registration for a workshop.

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
url = "https://api.zenoti.com/v1/workshops/workshop_id/registrations/registration_id/cancel"
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

