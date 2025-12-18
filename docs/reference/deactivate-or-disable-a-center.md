# Authentication

**Source:** https://docs.zenoti.com/reference/deactivate-or-disable-a-center

**Endpoint:** `/v1/Centers/deactivate_center`

---

## Description

This API will deactivate a center in an organization.

## Code Examples

### Python

```python
1
import requests
2
​
3
url = "https://api.zenoti.com/v1/Centers/deactivate_center"
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

