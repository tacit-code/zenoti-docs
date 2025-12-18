# Authentication

**Source:** https://docs.zenoti.com/reference/list-all-templates

**Endpoint:** `/v1/giftcards/templates?center_id={center_id}&giftcardtype={giftcardtype}&serviceOnly={serviceOnly}&fromOnline={fromOnline}&member_price={member_price}`

---

## Description

This API helps you to retrieve the list of gift card templates associated with the required center. You must specify the unique identifier of the center as center_id in the API request.

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
url = "https://api.zenoti.com/v1/giftcards/templates?serviceOnly=serviceOnly&fromOnline=fromOnline&member_price=member_price&guest_id=null&center_id=center_id&giftcardtype=giftcardtype"
4
​
5
headers = {
6
    "accept": "text/plain",
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

