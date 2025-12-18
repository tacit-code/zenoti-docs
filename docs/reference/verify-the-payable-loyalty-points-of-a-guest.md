# Authentication

**Source:** https://docs.zenoti.com/reference/verify-the-payable-loyalty-points-of-a-guest

**Endpoint:** `/v1/guests/{InvoiceId}/payments/loyalty_points/redeemable`

---

## Description

Use this API to check how many loyalty points and the loyalty amount (in $) that a guest can redeem while paying for an invoice.
You must specify appropriate details for the InvoiceId parameter. Optionally, you can provide the required values for the lp_program_id and redeem_across_programs parameters.

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
url = "https://api.zenoti.com/v1/guests/InvoiceId/payments/loyalty_points/redeemable?redeem_across_programs=0"
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

