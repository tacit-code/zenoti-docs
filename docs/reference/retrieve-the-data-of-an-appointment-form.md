# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-data-of-an-appointment-form

**Endpoint:** `/v1/appointments/{appointment_id}/forms_data?tag_Id={tag_id}&view_context={view_context}&version_no={version_no}`

---

## Description

This API helps you to retrieve the data for tag forms associated to the specified appointment. You must provide an appropriate identifier in the API request for the appointment_id parameter. You also need to specify the required details for three other parameters in the API request. Refer to the Request Parameters table for more information.

## Path Params

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

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
url = "https://api.zenoti.com/v1/appointments/appointment_id/forms_data?tag_Id=tag_id&view_context=view_context&version_no=version_no"
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

