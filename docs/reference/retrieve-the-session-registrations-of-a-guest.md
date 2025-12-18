# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-session-registrations-of-a-guest

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
url = "https://api.zenoti.com/Appointments/Sessions?UserId=user_id&StartDate=startDate&EndDate=endDate&CenterId=center_id&sorters={sorters[0].Property}&sorters={sorters[0].Ascending}"
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

