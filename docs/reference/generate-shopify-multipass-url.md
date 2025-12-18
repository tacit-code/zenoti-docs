# Authentication

**Source:** https://docs.zenoti.com/reference/generate-shopify-multipass-url

**Endpoint:** `/v1/ecommerce/shopify/multipass-url?user_id=${userId}&return_url=${returnUrl}`

---

## Description

The Generate Shopify Multipass URL API generates a Shopify Multipass token and returns the response object with multipass_url. This URL is used for redirecting the guests after a successful Shopify authentication.

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
url = "https://api.zenoti.com/v1/ecommerce/shopify/multipass-url?user_id=$userId&return_url=$returnUrl"
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

