# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-an-opportunity

**Endpoint:** `/v1/opportunities/{opportunity_id}`

---

## Description

Supply the unique identifier of the opportunity as opportunity_id and this API will retrieve the details of it.

## Path Params

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
url = "https://api.zenoti.com/v1/opportunities/opportunity_id"
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

