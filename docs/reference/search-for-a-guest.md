# Authentication

**Source:** https://docs.zenoti.com/reference/search-for-a-guest

**Endpoint:** `/v1/guests/search?center_id={center_id}&first_name={first_name}&last_name={last_name}&zip_code={zip_code}&phone={phone}&tags={tags}&user_name={user_name}&user_code={user_code}&email={user_email}`

---

## Description

This API helps you to search for a guest in the specified center or in the whole organization based on the Zenoti org level setting "Search Guest Across Centers".

## query parameters if you have a large number of records to be displayed. By default,

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `page` | string | - | - |
| `size` | string | - | - |
| `page` | string | - | - |
| `size` | string | - | - |
| `size` | string | - | - |

## Query Params

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
url = "https://api.zenoti.com/v1/guests/search?page=1&size=10&center_id=center_id&first_name=first_name&last_name=last_name&zip_code=zip_code&phone=phone&tags=tags&user_name=user_name&user_code=user_code&email=user_email"
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
response = requests.get(url, headers=headers)
11
​
12
print(response.text)
```

