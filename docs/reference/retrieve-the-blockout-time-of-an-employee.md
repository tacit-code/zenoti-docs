# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-blockout-time-of-an-employee

**Endpoint:** `/v1/blockouttimes/{block_out_time_id}?center_id={center_id}&expand[]=ReccuringDetails&source=0`

---

## Description

Use this API to retrieve the blockout time of the specified employee.

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
url = "https://api.zenoti.com/v1/blockouttimes/block_out_time_id?center_id=center_id&expand=ReccuringDetails&source=0"
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

