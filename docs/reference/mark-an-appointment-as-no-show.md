# Authentication

**Source:** https://docs.zenoti.com/reference/mark-an-appointment-as-no-show

**Endpoint:** `/v1/appointments/{appointment_group_id}/no_show`

---

## Description

This API helps you to mark an appointment as No-Show, if guests do not show up for their scheduled appointment.

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
url = "https://api.zenoti.com/v1/appointments/appointment_group_id/no_show"
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

## Responses

- **400**: Error
- **400**: Error

