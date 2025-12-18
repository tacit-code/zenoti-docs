# Authentication

**Source:** https://docs.zenoti.com/reference/mark-the-status-of-an-appointment-as-checked-in

**Endpoint:** `/v1/appointments/{appointment_group_id}/check_in`

---

## Description

This API helps you to mark the status of an appointment as checked-in. By doing so, you can provide your guests the option to self check-in for their scheduled appointments from your CMA and custom Webstore.

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
url = "https://api.zenoti.com/v1/appointments/appointment_group_id/check_in"
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

