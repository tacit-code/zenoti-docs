# Authentication

**Source:** https://docs.zenoti.com/reference/update-a-guest

**Endpoint:** `/v1/guests/{guest_id}`

---

## Description

Use this API to update the details of a guest. To update the details of a guest, modify the expanded guest object and supply it to this API. In return, you will receive the modified guest object. Note: You must send all the fields obtained from the Retrieve guest details API, even if you want to change the details of only one field. This API also allows guests to update another guest details provided they have a relationship defined in Zenoti. Also, only a host guest token can make changes to another guest.

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
response = requests.put(url, headers=headers)
12
​
13
print(response.text)
```

