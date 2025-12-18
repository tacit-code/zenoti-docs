# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-list-of-appointments-of-a-center

**Endpoint:** `/v1/appointments`

---

## Description

This API retrieves the list of all appointments of the specified center between the start date and end date.

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
url = "https://api.zenoti.com/v1/appointments"
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

