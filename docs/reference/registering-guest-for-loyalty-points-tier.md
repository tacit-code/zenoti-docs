# Authentication

**Source:** https://docs.zenoti.com/reference/registering-guest-for-loyalty-points-tier

**Endpoint:** `/v1/guests/1b6282ac-979a-48f6-900a-6fd5a57d46f5/tier`

---

## Description

This API registers a specified guest to a loyalty points program based on their eligibility for a tier. It can also assign the guest to the highest tier upon request.

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
url = "https://api.zenoti.com/v1/guests/1b6282ac-979a-48f6-900a-6fd5a57d46f5/tier"
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
response = requests.post(url, headers=headers)
12
​
13
print(response.text)
```

