# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-details-of-an-appointment

**Endpoint:** `/v1/appointments/{appointment_id}`

---

## Description

This API retrieves the details of the specified appointment. You must specify appropriate data for the appointment_id parameter.

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
url = "https://api.zenoti.com/v1/appointments/appointment_id"
4
​
5
headers = {
6
    "accept": "application/json",
7
    "content-type": "application/json",
8
    "Authorization": "apikey <your api key>"
9
}
10
​
11
response = requests.get(url, headers=headers)
12
​
13
print(response.text)
```

