# Authentication

**Source:** https://docs.zenoti.com/reference/fetch-collections-report

**Endpoint:** `/v1/reports/collections/flat_file`

---

## Description

This API gets the collections details in the organization during a selected date range.

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
url = "https://api.zenoti.com/v1/reports/collections/flat_file"
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

