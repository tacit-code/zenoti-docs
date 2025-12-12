# api-rate-limits-1

**Source:** https://docs.zenoti.com/docs/api-rate-limits-1

---

## Rate limit response headers

## Manage rate limits

Rate limiting is a mechanism to limit network traffic. Rate limiting reduces strain on web servers and limits how often you can repeat an action within a specific timeframe. Zenoti uses rate limits to ensure faster API response times and to maintain overall stability. If we receive a large quantity of API call requests within a small period, those requests may be throttled.

The following table lists sample response headers that are displayed when only the organization (account)-level limit is defined in your organization and rate limit is enabled.

The interpretation of the Rate limit response headers is as follows:

For a detailed explanation of the use cases of different request policies and the interpretation of the respective values of the Rate Limit Response Headers, refer to this Help article.

The standard applicable rate limit is 60 calls per minute. To opt for a higher-volume API rate limit, reach out to your Zenoti account manager and the relevant team will share the available add-on options with you

To avoid reaching your rate limits, you must make only the essential requests that you require.
Here are a few strategies that can help you to reduce the number of requests and avoid getting rate-limit exception responses.

Updated almost 3 years ago

- For a detailed explanation of the use cases of different request policies and the interpretation of the respective values of the Rate Limit Response Headers, refer to this Help article.
- The standard applicable rate limit is 60 calls per minute. To opt for a higher-volume API rate limit, reach out to your Zenoti account manager and the relevant team will share the available add-on options with you

- Eliminate unnecessary API calls
Optimize your code to only fetch the data that your app requires.
- Cache frequently used data
You can cache data on the server or the client by using DOM storage. You can also save relatively static information in a database or serialize it in a file. For example, you can cache the list of services, therapists performing the services, and their pricing details for a service booking workflow.
- Use Retry Logic
You can implement Retry logic after a certain amount of time if you receive an API rate limit exception as a response. For instance, Zenoti recommends that you verify the API responses after each API call you make. If you get an API rate limit exception, you must implement the Sleep option for some time and then try again. You should include code that catches errors. If you ignore such API rate limit exception errors and continue to make requests, your app will not be able to recover gracefully. You can use the Retry-After header if you receive a 429 response for the back-off time. Alternatively, you can use metadata (included with all API responses) for your app’s API usage to dynamically control the app’s behavior.
- Queue API requests
To queue your API requests use any one of several cloud applications available in the market. Here are a few cloud applications worth trying- * Amazon Simple Queue Service,Apache ActiveMQ, and Rackspace Cloud Queues API 1.0.

| Name | Value |
|---|---|
| Organization-RateLimit-Limit | 60;w=60;b=60 |
| RateLimit-Remaining | 48 |
| RateLimit-Reset | 50 |

| Response header | Description |
|---|---|
| Organization-RateLimit-Limit | 60;w=60;b=60
This indicates that the refill rate is 60 calls per 60 seconds (where w=60 sec). After every 1 minute, 60 calls are added to the bucket.b=60 indicates the maximum number of calls that can get accumulated over time is 60. Even if you do not make any API call for 2 hours, a maximum of 60 calls are accumulated. No more call accumulation can occur beyond this value. |
| RateLimit-Remaining | The value of this response header indicates the number of remaining API calls that you can make within that particular 48 seconds. This value continuously gets updated after every API call you make and is refreshed after the end of every 48 seconds. |
| RateLimit-Reset | The value of this response header indicates the time in seconds for the next refill of API calls. If the value is 50, it means that the rate limit will be refreshed to the maximum value of 60 after 50 seconds. |

