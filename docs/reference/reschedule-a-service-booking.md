# Authentication

**Source:** https://docs.zenoti.com/reference/reschedule-a-service-booking

**Endpoint:** `/v1/bookings`

---

## Description

Use this API to reschedule a service booking.

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
url = "https://api.zenoti.com/v1/bookings"
4
​
5
payload = {
6
    "center_id": "{{center_id}}",
7
    "date": "2019-09-13",
8
    "is_only_catalog_employees": "false",
9
    "guests": [
10
        {
11
            "id": "{{login_user_id}}",
12
            "invoice_id": "{{invoice_id}}",
13
            "items": [
14
                {
15
                    "item": { "id": "{{service_id}}" },
16
                    "therapist": { "id": "{{therapist_id}}" },
17
                    "invoice_item_id": "{{invoice_item_id}}"
18
                }
19
            ]
20
        }
21
    ]
22
}
```

