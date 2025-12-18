# Authentication

**Source:** https://docs.zenoti.com/reference/undo-the-check-in-of-a-guest-to-a-class

---

## Description

Use this API to undo the guest's check-in to your class. You can only undo the check-in of guests who are already checked in.

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
url = "https://api.zenoti.com/classes/class_id/registrations/registration_id/undo_sign_in"
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

