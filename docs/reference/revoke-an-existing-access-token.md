# Authentication

**Source:** https://docs.zenoti.com/reference/revoke-an-existing-access-token

**Endpoint:** `/v1/tokens/sessions/revoke`

---

## Description

Purpose: At any point of time, if you want to delete the existing access tokens, you can use this API to do so. This will immediately revoke all the existing access tokens and users cannot access the Zenoti APIs.

## Code Examples

### Python

```python
1
import requests
2
​
3
url = "https://api.zenoti.com/v1/tokens/sessions/revoke"
4
​
5
headers = {"accept": "text/plain"}
6
​
7
response = requests.delete(url, headers=headers)
8
​
9
print(response.text)
```

