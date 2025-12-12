# onboarding

**Source:** https://docs.zenoti.com/docs/onboarding

---

## 📘

## 🚧

Backend app
You need a backend app to get data and update the Zenoti API endpoints. Create individual apps for your use cases and modules. Assume you want to create an app for gift cards in Zenoti; create a backend app with the read/write permissions assigned on the gift cards module.

Create individual apps for individual use cases. A generic app with global permissions to all modules can lead to issues in debugging errors and pose a security threat if many users use the same app with a single API key.

Prerequisite
Before you start using the Zenoti API, do the following:

Updated over 2 years ago

- Ensure to enable the following role permissions:

At the organization level, click the Admin icon. 
Navigate to Organization > Security Roles. 
Select a role and go to Permissions. 
Expand Administrator. 
For API, select Manage API Keys, Manage Apps, and Manage Automation check boxes. 
Click Save.
- Create a backend app. To do this, go to organization level, Admin > Setup > Apps and follow the instructions.
- Generate a new API key.
- Use the API key or access token to make API calls.

- At the organization level, click the Admin icon.
- Navigate to Organization > Security Roles.
- Select a role and go to Permissions.
- Expand Administrator.
- For API, select Manage API Keys, Manage Apps, and Manage Automation check boxes.
- Click Save.

- Application ID and secrets are required to generate bearer tokens. Else, you can use the API key.
- The API key is valid for one year, after which you must update the API key before expiry.
- The bearer token is valid for 10 hours.

- Create the backend app and generate a new API key
- Update the existing API key

