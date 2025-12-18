# Authentication

**Source:** https://docs.zenoti.com/reference/center-services

**Endpoint:** `/v1/centers/{center_id}/services/{service_id}/therapists?`

---

## Description

This API allows you to retrieve the details of all the therapists who can perform a particular service at a center. We can also filter on the basis of whether the catalog for the therapist is enabled or not.

## Path Params

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
url = "https://api.zenoti.com/v1/centers/center_id/services/service_id/therapists"
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

