# Authentication

**Source:** https://docs.zenoti.com/reference/merge-guests

**Endpoint:** `/v1/guests/{target_guest_id}/merge`

---

## Description

This API helps you merge other guest details into the target guest.

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
url = "https://api.zenoti.com/v1/guests/target_guest_id/merge"
4
​
5
headers = {
6
    "accept": "application/json",
7
    "content-type": "application/json"
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

