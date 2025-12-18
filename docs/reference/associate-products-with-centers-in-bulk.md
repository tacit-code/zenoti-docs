# Authentication

**Source:** https://docs.zenoti.com/reference/associate-products-with-centers-in-bulk

---

## Description

This API enables bulk association of multiple products to centers in a single request, streamlining product-center mapping at scale.

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
url = "https://api.zenoti.com/api_url/v2/products/product_center_associations"
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
response = requests.put(url, headers=headers)
12
​
13
print(response.text)
```

