# Authentication

**Source:** https://docs.zenoti.com/reference/list-all-relationships-belonging-to-a-guest

**Endpoint:** `/v1/guests/{guest_id}/relationships`

---

## Description

This API retrieves all the relationships of a guest. For example, spouse, friend, etc. This allows you to view a list of all the family members of the guest.

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
url = "https://api.zenoti.com/v1/guests/guest_id/relationships"
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

