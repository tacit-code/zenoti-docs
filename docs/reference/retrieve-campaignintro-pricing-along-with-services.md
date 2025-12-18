# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-campaignintro-pricing-along-with-services

**Endpoint:** `/v1/Centers/{center_id}/services`

---

## Description

This API fetches services from the requested center. Based on certain query parameters like campaign_id and campaign_code, you can get additional information such as campaign-based discounted price information of the services.

## This API fetches services from the requested center. Based on certain query parameters like campaign_id and campaign_code, you can get additional information such as campaign-based discounted price information of the services.

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
url = "https://api.zenoti.com/v1/Centers/center_id/services"
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

