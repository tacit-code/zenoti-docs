# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-loyalty-points-history-of-a-guest

**Endpoint:** `/v1/guests/{guestId}/points?view_grooming_points={view_grooming_points}&page_num={page_num}&num_records={num_records}&expand[0]={expand[0]}`

---

## Description

This API helps you to retrieve the loyalty points history of the specified guest.

## query parameters if you have a large number of records to be displayed. By default,

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `guest_id` | string | - | - |
| `page_num` | string | - | - |
| `num_records` | string | - | - |
| `page_num` | string | - | - |
| `num_records` | string | - | - |
| `num_records` | string | - | - |

## To retrieve "guest_points_details", you must specify "expand[0]=get_points_history" in the query parameters as illustrated in the example.

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
url = "https://api.zenoti.com/v1/guests/guestId/points?page_num=page_num&num_records=num_records&sort_ascending=true&view_grooming_points=view_grooming_points&expand=expand[0]"
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

