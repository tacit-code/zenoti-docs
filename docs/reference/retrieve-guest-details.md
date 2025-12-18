# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-guest-details

**Endpoint:** `/v1/guests/{guest_id}`

---

## Description

This API helps you to retrieve the details of a guest who has previously been created. You must specify the unique identifier of the guest as guest_id in the API request.This API also allows guests to view the details of another guest, provided they have a relationship defined in Zenoti. Also, only a host guest token can view another guest's details.

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
url = "https://api.zenoti.com/v1/guests/guest_id"
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

