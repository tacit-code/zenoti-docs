# authentication

**Source:** https://docs.zenoti.com/docs/authentication

---

## API keys vs token-based authentication

## API-key-based authentication

## 📘Note

## Token based authentication

## 📘Note

The API authentication process validates the identity of the client attempting to make a connection by using an authentication protocol. The protocol sends the credentials of the remote client requesting the connection to the remote access server either in plain text or encrypted form.
Authentication is mandatory to access the Zenoti API. Zenoti API determines if you are a valid app user based on authentication headers in the API requests. Zenoti supports two types of authentication:

In the following table, we list the differences between the two authentication types and suggest scenarios for each authentication type.

Assume your API Key is "1fa75c01e77b497fa2a794473d1324713192fee3f19342b8bc4ca458023cab68". Enter "Authorization" as key and value as  "apikey 1fa75c01e77b497fa2a794473d1324713192fee3f19342b8bc4ca458023cab68" in the Header of the API request.

Note

API keys are confidential and should be stored on your servers.

In addition to the API Key authentication described above, you can use token-based authentication.

Note

Access token of an employee expires once the employee's password is changed or if an employee has left the organization.

The response contains an access_token to authenticate the APIs. The response also includes expiry.

Updated almost 3 years ago

- API key based - Use API keys across all APIs
- Token based - Use access tokens generated from login credentials

- In Zenoti from the organization level, go to Admin > Setup > Apps.
- Generate an API Key.
- Copy the API Key and replace it in the header of the API request. Add the key as the value in the Authorization header.

- For token-based authentication, you must generate an access token first. For access token generation, see the API reference.
- Use this token for your subsequent API calls.
- In the authorization header, provide the value as bearer {{access_token}}

- Generate an access token
- Refresh access token - Refresh the existing token so that it is valid and is not expired
- Revoke or delete a token - Delete the access token of a user/employee

| API key | Token based |
|---|---|
| Used to access the global master data
No restrictions on any API usage | Used to access module or role-based data
Restricted access based on app user's role in the organization |
| Easy to maintain - API keys are valid across all the apps. | Maintenance overhead - Access tokens expire and you must generate a refresh token. |
| Useful for server-side interactions.
For example: You have an internal app that talks to your backend server and integrates with Zenoti, API Keys are best suited for this scenario. | Useful for client-side interactions.
For example: You have a specific app for a guest or therapist. Based on the end user login credentials, you can generate an access token for the specific user. |
| Security - Less secure as API keys can access all APIs.
API keys don't expire and once it is stolen, they can be used until you rotate or revoke the key. | Security - More secure as access tokens expire after a certain period.
App users can only access apps where they are authorized. |

```json
**apikey {{api_key}}** 
  Replace the api_key with your generated API Key.
```

```
bearer {{access_token}}
```


## Code Examples

```
**apikey {{api_key}}** 
  Replace the api_key with your generated API Key.
```

```
**apikey {{api_key}}** 
  Replace the api_key with your generated API Key.
```

```
bearer {{access_token}}
```

