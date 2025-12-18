# Authentication

**Source:** https://docs.zenoti.com/reference/delete-relationship-between-guests

---

## Description

The purpose of this API is to delete the relationship between two guests.

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
url = "https://api.zenoti.com/%20v1/guests/guest_id/relationships/guest_relationship_id"
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
response = requests.delete(url, headers=headers)
11
​
12
print(response.text)
```

