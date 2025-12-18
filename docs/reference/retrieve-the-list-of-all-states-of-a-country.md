# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-list-of-all-states-of-a-country

**Endpoint:** `/v1/countries/{country_id}/states`

---

## Description

This API retrieves the list of all states of the specified country.

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
url = "https://api.zenoti.com/v1/countries/country_id/states?add_defaults_for_dropdown=false"
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

