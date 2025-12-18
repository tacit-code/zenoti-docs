# Authentication

**Source:** https://docs.zenoti.com/reference/create-a-gift-card-template-with-services-or-day-packages

**Endpoint:** `/v1/giftcards/templates/custom`

---

## Description

Supply the request body and this API will generate a custom gift card template with specified combination of services and day packages.

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
url = "https://api.zenoti.com/v1/giftcards/templates/custom"
4
​
5
headers = {
6
    "accept": "text/plain",
7
    "content-type": "application/json",
8
    "Authorization": "apikey <your api key>"
9
}
10
​
11
response = requests.post(url, headers=headers)
12
​
13
print(response.text)
```

