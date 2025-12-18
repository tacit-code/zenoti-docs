# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-sales-report-of-a-center

**Endpoint:** `/v1/sales/salesreport?center_id={center_id}&start_date={start_date}&end_date={end_date}&item_type={item_type}&status={status}`

---

## Description

NOTE : This API is deprecated. Requesting not to use this API for any new integrations as the data cannot be reconciled to new sales accrual/sales cash reports available in the UI. This API retrieves the list of sales of the specified center during the selected date range.You must specify appropriate details for the center_id, start_date, and end_date parameters in the API request.Note : The date range that you specify cannot be more than seven days.

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
url = "https://api.zenoti.com/v1/sales/salesreport?center_id=center_id&start_date=start_date&end_date=end_date&item_type=item_type&status=status"
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

