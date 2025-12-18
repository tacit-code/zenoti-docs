# Authentication

**Source:** https://docs.zenoti.com/reference/list-all-occasions

**Endpoint:** `/v1/giftcards/occasions`

---

## Description

This API will retrieve the list of occasions defined in your organization.

## Code Examples

### Python

```python
1
import requests
2
​
3
url = "https://api.zenoti.com/v1/giftcards/occasions"
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

