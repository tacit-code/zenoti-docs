# Authentication

**Source:** https://docs.zenoti.com/reference/center-memberships

**Endpoint:** `/v1/centers/{center_id}/memberships`

---

## Description

Supply unique identifier of the center as center_id and this API will retrieve the list of memberships associated with that center if the membership falls within the active sale period.

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
url = "https://api.zenoti.com/v1/centers/center_id/memberships?show_in_catalog=true&expand=Null"
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

