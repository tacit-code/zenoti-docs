# Authentication

**Source:** https://docs.zenoti.com/reference/metadata-of-the-opportunities

**Endpoint:** `/v1/opportunities/metadata/{section}`

---

## Description

Gives MetaData of the Opportunities which can be needed while creating an opportunity.
Different sections under metadata are :

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
url = "https://api.zenoti.com/v1/opportunities/metadata/1"
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

