# Authentication

**Source:** https://docs.zenoti.com/reference/update-appointment-progress-start-open-or-complete

**Endpoint:** `/v1/appointments/{appointment_id}/progress`

---

## Description

This API marks the progress of an appointment as start, open, or complete.

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
url = "https://api.zenoti.com/v1/appointments/appointment_id/progress"
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
response = requests.put(url, headers=headers)
12
​
13
print(response.text)
```

