# pagination

**Source:** https://docs.zenoti.com/docs/pagination

---

## Query parameters

## 📘

## 📘

## Response

## Error

API endpoints may return list or collection values that run into multiple pages. You can paginate the response objects to enable easy reading of the response. You can set the page and size limits by passing query parameters in your endpoint.

Pass page and size as query parameters to display multiple records. The default value for page is 1, and for size, it is 10.

Default: 1

In the example above, the API call will return a list of centers on 1 page with 20 records on each page.

Default: 10
Values range: 1-100
The maximum number of records per page cannot be more than 100.

The response displays a page_info object which gives you the total number of records, the page you are on, and the page size.

The page_info object contains the following:

Total: The total number of records in the system.
Page: The page that you are currently on.
Size: The number of records on each page.

You cannot request more than 100 resources at the same time. An error with code 422 is sent back if the limit is higher than 100.
Object that contains error message and error code details.

Updated over 3 years ago

- Page: The number of pages that you request in a query.

- Size: Determines the number of rows of data or the number of records per page in the response.

- page_info Object: This object contains information on all the page-related elements.

```
curl --location -g --request GET '{{api_url}}/v1/centers/{{center_id}}/products?page=1&size=20' \ --header 'Authorization: bearer {{access_token}}'
```

```json
"page_info": {
    "total": 27,
    "page": 1,
    "size": 10
  }
```

```
{ 
      "code":422, 
      "message":"You cannot request more than 100 items." 
    }
```


## Code Examples

```
curl --location -g --request GET '{{api_url}}/v1/centers/{{center_id}}/products?page=1&size=20' \ --header 'Authorization: bearer {{access_token}}'
```

```
curl --location -g --request GET '{{api_url}}/v1/centers/{{center_id}}/products?page=1&size=20' \ --header 'Authorization: bearer {{access_token}}'
```

```
"page_info": {
    "total": 27,
    "page": 1,
    "size": 10
  }
```

