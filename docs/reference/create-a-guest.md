# Authentication

**Source:** https://docs.zenoti.com/reference/create-a-guest

**Endpoint:** `/v1/guests`

---

## Description

This API helps you to create a guest. To create a new guest, you must fill the available details of the guest along with the mandatory fields that are set in the organization guest settings and then supply that guest object. In return, you will receive the guest object along with the unique identifier of the guest. Refer to the examples to know the minimum and maximum details required to create a guest.

## Query Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Guest object supports multiple parameters like tags, referrals, address_info, preferences, and login_info. Pass the required parameters using expand query parameter to include the same in the response.

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
url = "https://api.zenoti.com/v1/guests"
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
response = requests.post(url, headers=headers)
12
​
13
print(response.text)
```

