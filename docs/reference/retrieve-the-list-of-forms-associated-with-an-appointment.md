# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-list-of-forms-associated-with-an-appointment

**Endpoint:** `/v1/appointments/{appointment_id}/forms`

---

## Description

This API helps you to fetch the list of forms that are available for the specified appointment.

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
url = "https://api.zenoti.com/v1/appointments/appointment_id/forms"
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

