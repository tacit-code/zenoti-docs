# Authentication

**Source:** https://docs.zenoti.com/reference/validate-npi-details-of-a-prescriber

**Endpoint:** `/v1/eprescription/npi/{npi_number}/validate`

---

## Description

This API will validate the NPI number of prescribers before initiating onboarding to ePrescribe.

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
url = "https://api.zenoti.com/api_url/v1/eprescription/npi/npi_number/validate"
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

