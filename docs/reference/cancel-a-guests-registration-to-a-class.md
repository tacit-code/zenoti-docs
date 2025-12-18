# Authentication

**Source:** https://docs.zenoti.com/reference/cancel-a-guests-registration-to-a-class

**Endpoint:** `/v1/classes/{class_id}/registrations/{registration_id}/cancel`

---

## Description

Purpose: The purpose of this API is to cancel the registration of a user to a class.

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
url = "https://api.zenoti.com/v1/classes/class_id/registrations/registration_id/cancel"
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

