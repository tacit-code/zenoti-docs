# webhook-failure-handling

**Source:** https://docs.zenoti.com/docs/webhook-failure-handling

---

Webhook timeout
Each webhook request is queued for 10 seconds to get a response from the endpoint URL. If no response is received within 10 seconds, the request will attempt to reconnect to the server up to 5 times.

Webhook retry
The retry mechanism sends the webhook up to 5 times before failing with exponential backoff. Webhooks will wait for a minimum retry delay of 30 seconds to a maximum retry delay of 10 minutes between each attempt.

Automatic Webhook Deactivation
If a webhook fails up to 20 times in a row, it generates an error log, deactivates the webhook, and sends a failure notification email automatically.

You will receive an email as shown below.

Follow the given steps to resolve this issue:

Updated over 1 year ago

- Check whether the destination URL is operational or not.
- Examine the Webhook Failure Logs.
- Fix the errors in the destination URL.
- Re-enable the webhook.

| Due to a series of delivery failures, the webhook {WebhookName} has been temporarily deactivated. Please verify that the destination URL is working and resolve the webhook errors which are listed in the below link.
{WebhookFailureLogURL}After resolving the webhook errors, you can activate this webhook from inactive tab of webhooks page |
|---|

