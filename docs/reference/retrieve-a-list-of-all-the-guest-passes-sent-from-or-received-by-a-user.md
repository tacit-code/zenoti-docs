# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-a-list-of-all-the-guest-passes-sent-from-or-received-by-a-user

**Endpoint:** `/v1/guests/{guest_id}/guestpass`

---

## Description

The purpose of this API is to retrieve a list of all the guest passes sent from or received by a user. This includes Used, Received, and Available guest passes. You must specify the unique identifier of the guest who is sharing the guest pass guest_id, the item id for which the user wants to transfer to/receive from (default value would be null) instrument_id, the item type (default would be 1. 1: Membership) instrument_type, guest pass credit type (default would be 1. 1: Classes, 2: Visits, 0: Both) credit_type, type of user list the user requested (default would be 0. 0: Both, 1: Receiver, 2:Sender) list_type, and the expand parameter (expand[0]=available, expand[1]=received, expand[2]=used) expand.

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
url = "https://api.zenoti.com/v1/guests/guest_id/guestpass"
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

