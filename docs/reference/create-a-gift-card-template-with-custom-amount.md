# Authentication

**Source:** https://docs.zenoti.com/reference/create-a-gift-card-template-with-custom-amount

**Endpoint:** `/v1/giftcards/templates/custom`

---

## Description

Supply the request body and this API will generate a custom gift card template with specified amount.

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
    "accept": "application/json",
7
    "Authorization": "apikey <your api key>"
8
}
9
​
10
response = requests.post(url, headers=headers)
11
​
12
print(response.text)
```

