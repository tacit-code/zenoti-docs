# Authentication

**Source:** https://docs.zenoti.com/reference/cancel-a-service-booking

**Endpoint:** `/v1/invoices/{invoice_id}/cancel`

---

## Description

Use this API to cancel a service booking.

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
url = "https://api.zenoti.com/v1/invoices/invoice_id/cancel"
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
response = requests.put(url, headers=headers)
11
​
12
print(response.text)
```

