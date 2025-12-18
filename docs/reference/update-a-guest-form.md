# Authentication

**Source:** https://docs.zenoti.com/reference/update-a-guest-form

**Endpoint:** `/v1/Guests/{guest_id}/Forms`

---

## Description

This API helps you to update the details of a guest form for the specified guest.You must specify the unique identifier of the guest as guest_id in the API request.Note: Retrieving uploaded files, signatures and annoations are not supported.

## REQUEST BODY PARAMETERS

## Code Examples

### Python

```python
1
import requests
2
​
3
url = "https://api.zenoti.com/v1/Guests/guest_id/Forms"
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

