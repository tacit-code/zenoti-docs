# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-class-session-registrations-of-a-guest

---

## Description

This API helps you to retrieve the list of class sessions for which the specified guest has registered.

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
url = "https://api.zenoti.com/api/Appointments/Admin/Sessions?startDate=00%3A00%3A00&endDate=00%3A00%3A00"
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

