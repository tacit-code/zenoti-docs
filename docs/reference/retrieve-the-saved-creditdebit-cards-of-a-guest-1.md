# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-saved-creditdebit-cards-of-a-guest-1

---

## Description

This API helps you to retrieve the saved credit/debit cards of a guest at the specified center.

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
url = "https://api.zenoti.com/Guests/GuestId/CreditCardsOnFile?CenterId=CenterId&TransactionFrom=TransactionFrom"
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

