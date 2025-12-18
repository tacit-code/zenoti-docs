# Authentication

**Source:** https://docs.zenoti.com/reference/email-notifications-report-api

**Endpoint:** `/v1/reports/notifications/email/flat_file`

---

## Description

Purpose: The purpose of this API is to fetch a list of email notification details associated with a center.

## Query Params

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
url = "https://api.zenoti.com/v1/reports/notifications/email/flat_file"
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
response = requests.post(url, headers=headers)
12
​
13
print(response.text)
```

