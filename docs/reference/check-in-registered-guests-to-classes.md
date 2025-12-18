# Authentication

**Source:** https://docs.zenoti.com/reference/check-in-registered-guests-to-classes

---

## Description

Use this API to check-in registered guests to the classes.

## Path Params

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
url = "https://api.zenoti.com/classes/class_id/registrations/registration_id/sign_in"
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
response = requests.put(url, headers=headers)
11
​
12
print(response.text)
```

