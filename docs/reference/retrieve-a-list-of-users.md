# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-a-list-of-users

**Endpoint:** `/v1/marketing/target_segments/{target_segment_id}/guests`

---

## Description

This API retrieves a list of users that match specific rule criteria.

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
url = "https://api.zenoti.com/v1/marketing/target_segments/target_segment_id/guests"
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

