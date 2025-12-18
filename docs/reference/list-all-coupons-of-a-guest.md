# Authentication

**Source:** https://docs.zenoti.com/reference/list-all-coupons-of-a-guest

**Endpoint:** `/v1/guests/{guest_id}/coupons`

---

## Description

Provide unique identifier of the guest as guest_id and this api will retrieve the coupon history of the respective guest.
you can also use pagination by passing page and size query parameters if guest has huge number of records. By default page is set to 1 and size is set to 10. Size cannot be more than 100 which means maximum records per page cannot be more than 100.

## you can also use pagination by passing page and size query parameters if guest has huge number of records. By default page is set to 1 and size is set to 10. Size cannot be more than 100 which means maximum records per page cannot be more than 100.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `guest_id` | string | - | - |

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
url = "https://api.zenoti.com/v1/guests/guest_id/coupons"
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

