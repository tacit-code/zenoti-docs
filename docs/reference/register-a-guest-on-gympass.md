# Authentication

**Source:** https://docs.zenoti.com/reference/register-a-guest-on-gympass

**Endpoint:** `/v1/registrations?provider_id=Gympass`

---

## Description

Purpose: The purpose of this API is to register your guests on external providers like Gympass.

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
url = "https://api.zenoti.com/v1/registrations?provider_id=Gympass"
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

