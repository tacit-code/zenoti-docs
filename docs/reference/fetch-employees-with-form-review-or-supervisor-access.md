# Authentication

**Source:** https://docs.zenoti.com/reference/fetch-employees-with-form-review-or-supervisor-access

**Endpoint:** `/v1/Centers/{center_id}/employees/flat_file?employee_id={employee_id}&filter_by=is_forms_review_enabled&expand=is_supervisor`

---

## Description

This API retrieves a list of employees who have the necessary permissions to review a form or act as a supervisor

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
url = "https://api.zenoti.com/v1/Centers/center_id/employees/flat_file?employee_id=employee_id&filter_by=is_forms_review_enabled&expand=is_supervisor"
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

