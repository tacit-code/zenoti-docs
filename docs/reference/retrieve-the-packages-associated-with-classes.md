# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-packages-associated-with-classes

**Endpoint:** `/v1/classes/packages?search_type={search_type}&page={page}&size={size}&item_ids={item_ids}`

---

## Description

This API helps you to retrieve the packages that have a benefit associated with the specified class.

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
url = "https://api.zenoti.com/v1/classes/packages?search_type=search_type&page=page&size=size&item_ids=item_ids"
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

