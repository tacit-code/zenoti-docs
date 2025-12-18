# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-invoice-details

**Endpoint:** `/v1/invoices/{invoice_id}?expand=InvoiceItems&expand=Transactions`

---

## Description

Use this API to retrieve the details of an invoice. This API supports multiple expand parameters to retrieve more relevant information related to invoice like InvoiceItems, Appointments, Transactions, gst_parameters, and dues_and_fees

## Path Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Query Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## when the relevant parameters is passed in the expand query param the respective object information is retrieved in the response of this API. For every additional information you need the respective parameter needs to be passed.

## Code Examples

### Python

```python
1
import requests
2
​
3
url = "https://api.zenoti.com/v1/invoices/invoice_id?expand=InvoiceItems&expand=Transactions"
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

