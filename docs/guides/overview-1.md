# overview-1

**Source:** https://docs.zenoti.com/docs/overview-1

---

## What is a Webhook?

## Webhooks in Zenoti

## 📘To use Zenoti Webhooks, you need a subscription to the Zenoti API package. Reach out to your CSM to enable the package.

## How does it work?

## Webhook Events

A Webhook is an intermediary between two applications. It delivers data from one application to another application in real time. Unlike typical APIs (Application Programming Interface), where you must request information every time, Webhooks only require a single communication with an application. For every change in the application, the information is sent back, thus reducing the number of calls (communications) between the applications.

To better understand this, let us consider the following example:
Zenoti is a web application that hosts data about your guests, employees, and other operational information. You are currently working on a mobile app to monitor your daily appointments. If you are using an API, you must request information every time there is an update to the data. But if you use a Webhook, the data is updated in real-time and does not require the user to take any action.

Another example is the score ticker in Google. Every time there is a change in the score, Google reflects the change and shows the score in real-time. This is the basic purpose of a Webhook; providing information in real-time.

Zenoti Webhooks notify your application whenever it finds changes related to your business. For example, events such as the creation of a guest, an update to membership, or the closing of an invoice.

Zenoti Webhooks act as a bridge between your application and Zenoti to pass on the necessary information when an event occurs.

Protocol: Zenoti Webhooks use HTTP (Hyper Text Transfer Protocol), which is the standard for communications between two applications or servers. HTTP forms the main basis of communication for Zenoti Webhooks.

Verbs: The verbs specify an action performed on a specific resource. For example, if a new guest is created, Webhook uses the POST verb and adds the guest details.

The following verbs are used by Zenoti Webhooks:

To use Zenoti Webhooks, you need a subscription to the Zenoti API package. Reach out to your CSM to enable the package.

Using Webhooks in Zenoti is a three-step process.

Every time the selected event is triggered, Zenoti will notify your application about the change and provides an event response code.

Check the following response codes for all the events in Zenoti:

Zenoti Webhooks supports the following event types (Click the links to view the corresponding response codes):

Updated about 3 years ago

- POST
- PUT
- PATCH

- Event: Select an event in Zenoti; this is the event you want to track.
- Verb: Specify the verb for the event. For example, if you want to track the creation of new guests, select POST.
- URL: Get the Webhook URL from the application to which you want to send the data.

| Event Types | Event Names |
|---|---|
| Invoice | > Closed |
| Guest | > Created
> Updated
> Deleted |
| Class | > Schedule Created
> Schedule Updated
> Schedule Cancelled
> Schedule Deleted
> Booking Created
> Booking Cancelled
> Booking Deleted
> Booking Approved
> Booking No Show
> Booking Rejected |
| Guest Membership | > Created
> Freeze
> Unfreeze
> Cancelled
> Reinstate |
| Guest Package | > Creation
> Redemption
> Redemption Reversal
> Status Update
> Validity Update |
| Appointment | > Started
> Completed
> Feedback Created |
| Appointment Group | > Created
> Status |
| Employee | > Deleted
> Created
> Updated |

