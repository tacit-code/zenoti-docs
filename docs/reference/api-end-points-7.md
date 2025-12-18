# Authentication

**Source:** https://docs.zenoti.com/reference/api-end-points-7

**Endpoint:** `/v1/reasons`

---

## Description

This API retrieves the list of specific reasons that a center's front-desk executives can select from when they cancel a membership, cancel an appointment, or mark a guest as a turnaway.

## Query Params

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
url = "https://api.zenoti.com/v1/reasons"
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

