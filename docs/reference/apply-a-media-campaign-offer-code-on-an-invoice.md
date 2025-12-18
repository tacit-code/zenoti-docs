# Authentication

**Source:** https://docs.zenoti.com/reference/apply-a-media-campaign-offer-code-on-an-invoice

**Endpoint:** `/v1/invoices/{invoice_id}/campaign_discount/apply`

---

## Description

This API helps you to apply a media campaign offer code on an invoice. By doing so, you can provide your guests the option to avail promotional discounts on their invoice when they purchase any services or products from your Customer Mobile Application (CMA) or custom Webstore. For more information on how to configure a media campaign, refer to this Help article.

## Path Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

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
url = "https://api.zenoti.com/v1/invoices/invoice_id/campaign_discount/apply"
4
​
5
payload = {
6
    "offer_code": "offer_code",
7
    "center_id": "(center_id)"
8
}
9
headers = {
10
    "accept": "application/json",
11
    "content-type": "application/json",
12
    "Authorization": "apikey <your api key>"
13
}
14
​
15
response = requests.post(url, json=payload, headers=headers)
16
​
17
print(response.text)
```

