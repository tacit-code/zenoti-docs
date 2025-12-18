# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-schedules-of-employees-of-a-center

**Endpoint:** `/v1/centers/{center_id}/employee_schedules?start_date={start_date}&end_date={end_date}&schedule_status={schedule_status}&employee_id={employee_id}&job_id={job_id}&consider_schedule_time={consider_schedule_time}`

---

## Description

This API helps you to retrieve the schedules of employees of the specified center.
You must provide the unique identifier of the center as center_id. You must also specify the appropriate start_date and end_date values for which you want to view the schedules of employees.

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
url = "https://api.zenoti.com/v1/centers/center_id/employee_schedules?start_date=start_date&end_date=end_date&schedule_status=schedule_status&employee_id=employee_id&job_id=job_id&consider_schedule_time=consider_schedule_time"
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

