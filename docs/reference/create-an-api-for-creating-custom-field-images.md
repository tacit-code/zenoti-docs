# Authentication

**Source:** https://docs.zenoti.com/reference/create-an-api-for-creating-custom-field-images

**Endpoint:** `/v1/employees/images`

---

## Description

This API is created to upload employee custom field images to S3 bucket

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
url = "https://api.zenoti.com/v1/employees/images"
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

