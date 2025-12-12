# create-the-backend-app-and-generate-a-new-api-key-1

**Source:** https://docs.zenoti.com/docs/create-the-backend-app-and-generate-a-new-api-key-1

---

The steps in this article cater to the following audience:

Important: The process to generate and update an API key has changed.

Generate a new API key for each app. For example, if you have a Web Booking app and a Mobile Booking app, you must generate two API keys respectively.

This API Key will work only for the designated app. If you have multiple apps, you must generate separate API Keys for each app. Repeat this process from Step 1 for each app. Zenoti recommends that you create separate apps for each of your use cases. It is difficult to audit logs and troubleshoot issues if there are multiple users of the same app. Many users of a single app with a single API key also pose security concerns.

Updated over 1 year ago

- Businesses that are new to Zenoti and want to utilize its API functionality.
- Existing businesses that need to generate new API Keys for apps other than the Default app.

- Earlier navigation: At the organization-level, Admin > Setup > API.
- New navigation: 

At the organization level, click the Configuration icon.
Search for and select the Apps setting from the Integrations section.

- At the organization level, click the Configuration icon.
- Search for and select the Apps setting from the Integrations section.

- At the organization level, click the Configuration icon.
- Search for and select the Apps setting from the Integrations section.
- On the Manage Applications page, click Add .
- Enter the following information:

Name: Enter the name of the application.
URI: Enter the URL of your Website or the application. In case of errors or issues in the app, URL information is used to contact the app developer.
Description: Enter a brief description of the app for which you are generating the API key.
Login User Type: Select any one of the following

Guest: Select this check box if this is a guest-facing application and the login user is a guest.
Employee: Select this check box if this is an internal app and the login user is an employee of your business.


Source App: Select one of the following from the drop-down list:

External CMA: Select this option if the API is for the CMA. All the appointments booked from this application will be marked with the Mobile Booking icon. 
External Webstore: Select this option if the API is for Webstore. All the appointments booked from Webstore, will be marked with the Web Booking icon
Client App: Select this option if the API is for the client app of your business.
Bot: Select this option if the API is for a bot. All the appointments booked by the bot will be marked with the Bot Booking icon.


Post Logout Redirect URL: To redirect your users to a URL after they log out, click Add, and then enter the URL.
Post Login Redirect URL: To redirect your users to a URL after they log in, click Add, and enter the URL.
- Click Next.
- Manage the scope of your app by selecting the checkbox of data permissions under the appropriate API groups. For example, if you want to restrict access of the app to an employee module, then expand and select only the corresponding employee permissions under the relevant API group. Choose your authentication method - API keys (APIKEY GROUPS) or access tokens (JWT GROUPS) to authorize the app users.
- Click Next.
Zenoti generates a new Application ID and Secrets (secret key). These are used to generate a new API key.
- Copy the Application ID and the Secrets on a notepad.
Note: Make a note of the Application ID and the Secrets before you navigate away from this screen. If you navigate away from this page, you must restart the API generation process from the beginning.
- Click Generate API Key.
Zenoti generates a new API Key for your business and the app.
Note: The generated API keys expire in a designated time duration. You can configure an alert to be sent a set number of days before expiry. To send these alerts, you must configure the  Expiry of API keys alert for your business at the organization level.
- Copy the API key on a notepad.
- Click Finish.

- Name: Enter the name of the application.
- URI: Enter the URL of your Website or the application. In case of errors or issues in the app, URL information is used to contact the app developer.
- Description: Enter a brief description of the app for which you are generating the API key.
- Login User Type: Select any one of the following

Guest: Select this check box if this is a guest-facing application and the login user is a guest.
Employee: Select this check box if this is an internal app and the login user is an employee of your business.
- Source App: Select one of the following from the drop-down list:

External CMA: Select this option if the API is for the CMA. All the appointments booked from this application will be marked with the Mobile Booking icon. 
External Webstore: Select this option if the API is for Webstore. All the appointments booked from Webstore, will be marked with the Web Booking icon
Client App: Select this option if the API is for the client app of your business.
Bot: Select this option if the API is for a bot. All the appointments booked by the bot will be marked with the Bot Booking icon.
- Post Logout Redirect URL: To redirect your users to a URL after they log out, click Add, and then enter the URL.
- Post Login Redirect URL: To redirect your users to a URL after they log in, click Add, and enter the URL.

- Guest: Select this check box if this is a guest-facing application and the login user is a guest.
- Employee: Select this check box if this is an internal app and the login user is an employee of your business.

- External CMA: Select this option if the API is for the CMA. All the appointments booked from this application will be marked with the Mobile Booking icon.
- External Webstore: Select this option if the API is for Webstore. All the appointments booked from Webstore, will be marked with the Web Booking icon
- Client App: Select this option if the API is for the client app of your business.
- Bot: Select this option if the API is for a bot. All the appointments booked by the bot will be marked with the Bot Booking icon.

