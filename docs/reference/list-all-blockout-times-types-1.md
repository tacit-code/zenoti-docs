# Authentication

**Source:** https://docs.zenoti.com/reference/list-all-blockout-times-types-1

**Endpoint:** `/v1/organizations/blockouttimes/types?page=1&size=100&source=1`

---

## Description

Description
When providers are unavailable due to any reason such as lunch, training, or break, you can use Block Out Time Types to show their unavailability on the Appointment Book.
you can also use pagination by passing page and size query parameters if you have huge number of records by default page is set to 1 and size is set to 10. size cannot be more than 100 which means maximum records per page cannot be more than 100.

## you can also use pagination by passing page and size query parameters if you have huge number of records by default page is set to 1 and size is set to 10. size cannot be more than 100 which means maximum records per page cannot be more than 100.

## Code Examples

### Python

```python
1
import requests
2
​
3
url = "https://api.zenoti.com/v1/organizations/blockouttimes/types?page=1&size=100&source=1"
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

