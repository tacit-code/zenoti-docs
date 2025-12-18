# Authentication

**Source:** https://docs.zenoti.com/reference/retrieve-the-schedules-of-classes-in-multiple-centers

**Endpoint:** `/v1/classes/sessions?center_id={center_id}&page={page}&class_name={class_name}&start_date={start_date}&end_date={end_date}&show_in_catalog={show_in_catalog}&status={status}&registration_id={registration_id}&session_id={session_id}&filters[0].property={filters[0].property}&filters[0].value={filters[0].value}&filters[1].property={filters[1].property}&filters[1].value={filters[1].value}{&filters[2].property=}filters[2].property{&filters[2].value=}filters[2].value{&filters[3].property=}filters[3].property{&filters[3].value=}filters[3].value{&filters[4].property=}filters[4].property{&filters[4].value=}filters[4].value{&class_id=}class_id{&recurrence_id=}recurrence_id{&session_name=}session_name{&guest_id=}guest_id{&size=}size{}`

---

## Description

This API helps you to retrieve the list of active schedules of classes sessions in multiple centers.

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
url = "https://api.zenoti.com/v1/classes/sessions?center_id=center_id&page=page&class_name=class_name&start_date=start_date&end_date=end_date&show_in_catalog=show_in_catalog&status=status&registration_id=registration_id&session_id=session_id&filters={filters[0].property}&filters={filters[0].value}&filters={filters[1].property}&filters={filters[1].value}}&filters={filters[2].property}&filters={filters[2].value}&filters={filters[3].property}&filters={filters[3].value}&filters={filters[4].property}&filters={filters[4].value}&class_id=class_id&recurrence_id=recurrence_id&session_name=session_name&guest_id=guest_id&size=size"
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

