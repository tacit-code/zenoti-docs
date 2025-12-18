# Authentication

**Source:** https://docs.zenoti.com/reference/fetch-list-of-centers-based-on-parameters

**Endpoint:** `/v1/Centers`

---

## Description

This API retrieves a list of centers based on the base center's ID and coordinates (latitude and longitude).

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
url = "https://api.zenoti.com/api_url%20/v1/Centers"
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
response = requests.get(url, headers=headers)
12
​
13
print(response.text)
```

