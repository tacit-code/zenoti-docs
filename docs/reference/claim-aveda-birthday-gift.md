# Authentication

**Source:** https://docs.zenoti.com/reference/claim-aveda-birthday-gift

**Endpoint:** `/v1/guests/{guest_id}/aveda/birthday_gift`

---

## Description

This API claims an Aveda birthday gift for a specific guest using a valid offer code. It processes the gift through Aveda integration and updates the guest’s records.

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
url = "https://api.zenoti.com/v1/guests/guest_id/aveda/birthday_gift"
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

