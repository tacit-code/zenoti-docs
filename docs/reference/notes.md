# Authentication

**Source:** https://docs.zenoti.com/reference/notes

**Endpoint:** `/v1/opportunities/{opportunity_id}/notes`

---

## Description

Supply the unique id od the opportunity as opportunity_id and request body to this API and this API will add notes to that opportunity.

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
url = "https://api.zenoti.com/v1/opportunities/opportunity_id/notes"
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
response = requests.post(url, headers=headers)
11
​
12
print(response.text)
```

