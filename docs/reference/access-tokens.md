# Authentication

**Source:** https://docs.zenoti.com/reference/access-tokens

**Endpoint:** `/v1/tokens`

---

## Description

Purpose: The purpose of this API is to generate a new access token for the authentication of the user. Businesses can use this token to access Zenoti APIs.

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
url = "https://api.zenoti.com/v1/tokens"
4
​
5
payload = {
6
    "account_name": "account name",
7
    "user_name": "username",
8
    "password": "Enter your password",
9
    "grant_type": "password",
10
    "app_id": "DB6D3C87-7913-43E3-81B6-08B0F1708D09",
11
    "app_secret": "312a4d9488e04a829fe9dab88377e78f8e071240f3e241ca82e01c306e556599",
12
    "device_id": "c113476f-04e1-484c-b887-57414441cdcf"
13
}
14
headers = {
15
    "accept": "application/json",
16
    "content-type": "application/json"
17
}
18
​
19
response = requests.post(url, json=payload, headers=headers)
20
​
21
print(response.text)
```

