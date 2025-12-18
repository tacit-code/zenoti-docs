# Authentication

**Source:** https://docs.zenoti.com/reference/list-all-products-purchased-by-a-guest

**Endpoint:** `/v1/guests/{guest_id}/products`

---

## Description

Provide unique identifier of the guest as guest_id and this API will retrieve the products purchased by the guest.

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
url = "https://api.zenoti.com/v1/guests/guest_id/products"
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

