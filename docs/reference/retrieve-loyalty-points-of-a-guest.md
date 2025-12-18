# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-loyalty-points-of-a-guest

---

## Description

Use this API to retrieve the details of loyalty points of a guest.

## Code Examples

### Python

```python
1
import requests
2
​
3
url = "https://api.zenoti.com/"
4
​
5
headers = {"Authorization": "apikey <your api key>"}
6
​
7
response = requests.get(url, headers=headers)
8
​
9
print(response.text)
```

