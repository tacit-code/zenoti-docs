# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-list-of-all-countries

**Endpoint:** `/v1/countries`

---

## Description

This API retrieves the list of all countries.

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
url = "https://api.zenoti.com/v1/countries?add_defaults_for_dropdown=false"
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

