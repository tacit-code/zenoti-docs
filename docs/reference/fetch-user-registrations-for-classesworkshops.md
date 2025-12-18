# Authentication

**Source:** https://docs.zenoti.com/reference/fetch-user-registrations-for-classesworkshops

**Endpoint:** `/v1/guests/{guest_id}/registrations?start_date=2022-10-15&end_date=2022-10-18&class_type=1&filters.period=0&page=2&size=2&expand[0]=centers&expand[1]=instructors&expand[2]=sessions&expand[3]=classes`

---

## Description

Purpose: Use this API to fetch the user registrations to the classes or workshops.

## and the parameters mentioned in PATH PARAMS section.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `guest_id` | string | - | - |

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
url = "https://api.zenoti.com/v1/guests/guest_id/registrations?filters=all&expand=centers&expand=instructors&expand=sessions&expand=classes&sorters=&start_date=2022-10-15&end_date=2022-10-18&class_type=1&filters.period=0&page=2&size=2"
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

