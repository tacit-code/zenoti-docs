# Authentication

**Source:** https://docs.zenoti.com/reference/verify-the-balance-of-a-gift-card

**Endpoint:** `/v1/giftcards/{giftcard_number}/balance`

---

## Description

This API helps you to verify the balance of a guest's Zenoti gift card.

## Path Params

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
url = "https://api.zenoti.com/v1/giftcards/giftcard_number/balance"
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

