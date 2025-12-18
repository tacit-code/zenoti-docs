# Authentication

**Source:** https://docs.zenoti.com/reference/list-all-opportunities

**Endpoint:** `/v1/opportunities?view_id={center_id}&page_num={page_num}&records={records}&keywords={keywords}&owner={owner}&type={type}&guest_id={guest_id}&disposition_id={disposition_id}&followup_from_date={followup_from_date}&followup_to_date={followup_to_date}&creation_from_date={creation_from_date}&creation_to_date={creation_to_date}&status_id={status_id}&priority_id={priority_id}&source_id={source_id}&last_modified_start_date={last_modified_start_date}&last_modified_end_date={last_modified_end_date}`

---

## Description

Supply the unique identifier of the center and the fields on which you want to filter the opportunities and this API will return the list of opportunities in that center.

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
url = "https://api.zenoti.com/v1/opportunities?view_id=center_id&page_num=page_num&records=records&keywords=keywords&owner=owner&type=type&guest_id=guest_id&disposition_id=disposition_id&followup_from_date=followup_from_date&followup_to_date=followup_to_date&creation_from_date=creation_from_date&creation_to_date=creation_to_date&status_id=status_id&priority_id=priority_id&source_id=source_id&last_modified_start_date=last_modified_start_date&last_modified_end_date=last_modified_end_date"
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

