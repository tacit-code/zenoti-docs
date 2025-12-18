# Authentication

**Source:** https://docs.zenoti.com/reference/list-all-centers

**Endpoint:** `/v1/centers?expand=working_hours`

---

## Description

This API retrieves a list of all centers of an organization.

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
url = "https://api.zenoti.com/v1/centers?expand=working_hours"
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

