# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-list-of-security-roles-in-a-center

**Endpoint:** `/v1/organizations/security_roles?type={type}`

---

## Description

This API helps you to fetch the list of security roles in a center.

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
url = "https://api.zenoti.com/v1/organizations/security_roles?type=-3"
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

