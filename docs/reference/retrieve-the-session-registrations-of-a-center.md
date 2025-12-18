# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-session-registrations-of-a-center

---

## Description

This API helps you to retrieve the list of class session registrations in the specified center.

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
url = "https://api.zenoti.com/Appointments/Sessions/40747?SessionId=session_id&StatusString=StatusString"
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

