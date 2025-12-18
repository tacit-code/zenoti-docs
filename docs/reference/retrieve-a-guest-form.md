# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-a-guest-form

**Endpoint:** `/v1/Guests/{guest_id}/Forms?version_no={version_no}`

---

## Description

This API helps you to retrieve the specified guest's form data.You must specify the unique identifier of the guest as guest_id and the form's version_no in the API request.Note: Retrieving uploaded files, signatures and annoations are not supported.

## Path Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

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
url = "https://api.zenoti.com/v1/Guests/guest_id/Forms?version_no=version_no"
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

