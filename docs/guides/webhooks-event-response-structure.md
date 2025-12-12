# webhooks-event-response-structure

**Source:** https://docs.zenoti.com/docs/webhooks-event-response-structure

---

## Structure of an Event Response object

Any incoming Webhook response contains the following information:

Both the event data and the object data form the structure of the event response.

A sample structure of the Event Response object:

The structure contains the following elements:
a. Id: Identifies the Webhook call
b. event_id: Identifies the event type
c. event_schema: Object schema version of the resource of a corresponding event
d. event_resource: Name of the event. For example, Guest, Invoice
e. event_type: Name of the event type. For example, Guest Creation, Invoice Closed, etc
f. event_timestamp: Time and date when the event was triggered
g. data: Response object of the corresponding event

Updated about 3 years ago

- HTTP header: This is the header of the response and it contains a signature for verification and validation of the response.
- HTTP body: This is the body of the response and it contains the following as a JSON message:

Event data
Object data

- Event data
- Object data

```
{  
  "id": "622b5b33a961750e01db6512",  
  "event_id": "622b5b33a961750e01db6510",  
  "event_schema": "v1",  
  "event_resource": "Invoice",  
  "event_type": "Invoice.Closed",  
  "event_timestamp": "2022-03-11T14:22:43.3847049Z",  
  "data": {}  
}
```


## Code Examples

```
{  
  "id": "622b5b33a961750e01db6512",  
  "event_id": "622b5b33a961750e01db6510",  
  "event_schema": "v1",  
  "event_resource": "Invoice",  
  "event_type": "Invoice.Closed",  
  "event_timestamp": "2022-03-11T14:22:43.3847049Z",  
  "data": {}  
}
```

```
{  
  "id": "622b5b33a961750e01db6512",  
  "event_id": "622b5b33a961750e01db6510",  
  "event_schema": "v1",  
  "event_resource": "Invoice",  
  "event_type": "Invoice.Closed",  
  "event_timestamp": "2022-03-11T14:22:43.3847049Z",  
  "data": {}  
}
```

