# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-list-of-all-security-profiles

**Endpoint:** `/v1/organizations/security_roles?type=3`

---

## Description

The purpose of this API is to get a list of all the security profiles associated under the organization and under the center.

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
url = "https://api.zenoti.com/v1/organizations/security_roles?type=3"
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

