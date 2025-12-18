# Authentication

**Source:** https://docs.zenoti.com/reference/implement-single-therapist-bookings-for-v1

**Endpoint:** `/v1/bookings`

---

## Description

This API ensures that when consider_single_therapist_slot is set to true, all booked services are assigned to the same therapist.

## Code Examples

### Python

```python
1
import requests
2
​
3
url = "https://api.zenoti.com/api_url/v1/bookings"
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

