# Authentication

**Source:** https://docs.zenoti.com/reference/get-pay-cycle-settings-of-multiple-centers

**Endpoint:** `/v1/payroll/centers/pay_period_settings`

---

## Description

The purpose of the API is to fetch pay period settings for a list of centers in a given duration.

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
url = "https://api.zenoti.com/v1/payroll/centers/pay_period_settings"
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

