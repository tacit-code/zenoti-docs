# Authentication

**Source:** https://docs.zenoti.com/reference/undo-the-status-of-a-checked-in-appointment

**Endpoint:** `/v1/appointments/{appointment_group_id}/undo_check_in`

---

## Description

This API helps you to undo the status of a checked-in appointment. By doing so, you can provide your guests the option to undo the status of their self checked-in appointments from your CMA and custom Webstore.
You must specify appropriate data for the appointment_group_id parameter.

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
url = "https://api.zenoti.com/v1/appointments/appointment_group_id/undo_check_in"
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

