# Authentication

**Source:** https://docs.zenoti.com/reference/list-all-blockout-times-of-a-center

**Endpoint:** `/v1/centers/{center_id}/blockouttimes`

---

## Description

Retrives the list of Blockout times created between the start date and end date of the center whose ID is passed as {center_id} and block out times of all the rooms or employees who had a block out time created in the appointment book for that center.

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
url = "https://api.zenoti.com/v1/centers/center_id/blockouttimes?start_date=2023-06-01&end_date=2023-06-01&source=0"
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

