# response-and-error-codes

**Source:** https://docs.zenoti.com/docs/response-and-error-codes

---

Response
The API calls will respond with appropriate HTTP status codes for all requests. The response to every request is sent in JSON format.  If the API request results in an error, you get an "error": {error code and reason} key in the JSON response. For successful request, the error returns a null value.

Updated over 3 years ago

- 200 OK indicates a successful response.
- 4XX response indicates an error from the requesting client
- 5XX response indicates an error from our API servers.

