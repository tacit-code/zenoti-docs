# Authentication

**Source:** https://docs.zenoti.com/reference/get-center-predefined-gift-card-templates

**Endpoint:** `/v1/giftcards/templates`

---

## Description

This API retrieves the list of different types of predefined gift card templates for a given center.

## Body Params

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
url = "https://api.zenoti.com/v1/giftcards/templates"
4
​
5
headers = {
6
    "accept": "application/json",
7
    "content-type": "application/json",
8
    "Authorization": "apikey <your api key>"
9
}
10
​
11
response = requests.get(url, headers=headers)
12
​
13
print(response.text)
```

