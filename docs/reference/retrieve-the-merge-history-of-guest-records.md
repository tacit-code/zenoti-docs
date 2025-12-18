# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-merge-history-of-guest-records

**Endpoint:** `/v1/guests/merge_history?start_date={start_date}&end_date={end_date}&center_id={center_id}&page={page}&size={size}`

---

## Description

Use this API to fetch the merge history of guest records. This API also retrieves the history of guest records that have been merged across different centers.

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
url = "https://api.zenoti.com/v1/guests/merge_history?page=page&size=size&start_date=start_date&end_date=end_date&center_id=center_id"
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

