# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-a-list-of-all-the-guest-pass-users

**Endpoint:** `/v1/guests/{guest_id}/guestpass?instrument_id={instrument_id}&instrument_type={instrument_type}&list_type={list_type}&credit_type={credit_type}`

---

## Description

Purpose: Use this API to list all the users of the Guest Pass membership program.

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
url = "https://api.zenoti.com/v1/guests/guest_id/guestpass?instrument_type=instrument_type&list_type=list_type&credit_type=credit_type&instrument_id=instrument_id"
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

