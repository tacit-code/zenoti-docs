# Authentication

**Source:** https://docs.zenoti.com/reference/api-end-points-1

**Endpoint:** `/v1/employees`

---

## Description

This API helps you to create an employee profile, along with catalog information in a center.
Note: For information on how to update the details of a previously-created employee profile, click here.

## Request Body Parameters

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
url = "https://api.zenoti.com/v1/employees"
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

