# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-compliance-statistics

**Endpoint:** `/v1/organizations/treatment_forms/compliance_rule_statistics`

---

## Description

This API retrieves all compliance statistics of an organization.

## Query Params

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
url = "https://api.zenoti.com/api_url/v1/organizations/treatment_forms/compliance_rule_statistics?start_date=false&end_date=false"
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

