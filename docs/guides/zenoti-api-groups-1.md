# zenoti-api-groups-1

**Source:** https://docs.zenoti.com/docs/zenoti-api-groups-1

---

## 📘

Authorization is an additional security layer to check if you have permission to access the API endpoints. Your backend app's group permissions (JWT Groups and APIKEY Groups) govern the Authorization layer.

For more information, refer to step 5 in create backend app.

For example, you are an admin. You have an access token for a backend app to retrieve guest information. Based on your role permission, API access will return an error. Similarly, if your backend app has given you access to employee read data, you will be blocked from updating employee data.

API calls will first check if you have the security role permission to access the data. Next, it checks the group permissions of your backend app. If you have the group permissions but do not have the security role permission to access a module, the system will throw an error.

Updated almost 3 years ago

