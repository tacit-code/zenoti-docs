# Authentication

**Source:** https://docs.zenoti.com/reference/insert-guests-feedback-into-zenoti

**Endpoint:** `/v1/appointments/{appointment_group_id}/feedbacks`

---

## Description

This API inserts a guest's feedback (which has been collected by using a third-party software) on a specific appointment into Zenoti.

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
url = "https://api.zenoti.com/v1/appointments/appointment_group_id/feedbacks"
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
response = requests.post(url, headers=headers)
11
​
12
print(response.text)
```

