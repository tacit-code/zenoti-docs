# api-for-custom-sources

**Source:** https://docs.zenoti.com/docs/api-for-custom-sources

---

## What are custom sources in Zenoti?

The custom sources in Zenoti are the places from where an appointment can be booked. These are as follows:

Consumer Mobile App (CMA)
Webstore
Client App
Bot

A business can receive bookings from any of the custom sources in Zenoti. The icons on the appointment block indicate the source of the booking. These help you identify the source of API calls and troubleshoot in case of issues.

As per the source you specify in the backend app, your API calls map to the respective custom source in Zenoti.

Updated almost 3 years ago

- Consumer Mobile App (CMA)

- Webstore

- Bot

| Follow these steps: |
|---|
| 1. Create a backend app and have the App ID, App Secret, and API Key handy. |
| 2. Make API calls and pass the generated API Key in the authorization parameter. This automatically maps to the corresponding source of the app. Be it External-Webstore, External-CMA, or Bot the respective icon appears on reports or Zenoti Web to identify the source. |
| 3. You can add an additional security layer to authorize API calls using a bearer token. The calls you make using the bearer token automatically maps to the corresponding custom source. |
| 4. Contact your Zenoti Customer Service Manager (CSM) in the following cases:- Get credentials for a custom source app - Enable API package in your organization - Contact your organization's admin, if you have API enabled but cannot see the Apps page. |

