# Authentication

**Source:** https://docs.zenoti.com/reference/list-all-memberships-of-a-guest

**Endpoint:** `/v1/guests/{guest_id}/memberships?center_id={center_id}`

---

## Description

This API helps you to retrieve the membership history of the respective guest.  You must specify the unique identifier of the guest as guest_id in the request.  If you want to breakdown the list of memberships by their status, you must pass the expand parameter is_active.  If you are using api_key to retrieve the data, it is mandatory to specify the center_id details in the request.

## Path Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Query Params

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
url = "https://api.zenoti.com/v1/guests/guest_id/memberships?is_active=Status%20of%20the%20membership&center_id=center_id"
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

