# Authentication

**Source:** https://docs.zenoti.com/reference/list-the-series-packages-of-a-guest

**Endpoint:** `/v1/guests/guest_id/Packages?center_id={center_id}&show_redeemable={true/false}&page_num={page_num}&page_size={page_size}`

---

## Description

This API lists the details of the Series packages that a particular guest has bought or redeemed from a specific center.

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
url = "https://api.zenoti.com/v1/guests/guest_id/Packages?center_id=center_id&show_redeemable={true/false}&page_num=page_num&page_size=page_size"
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

