# Python Requests: Simple Tasks with Randommer API

This exercise set will help you practice using the `requests` library in Python to interact with APIs that require custom headers and an API key. We will use the [Randommer API](https://randommer.io/api) for these tasks.

---

## Step 1: Create a Randommer.io Account and Get Your API Key

Before you start, you need to sign up for a free account on Randommer.io and get your API key:

1. Go to [https://randommer.io/](https://randommer.io/)
2. Click on "Sign Up" and create a new account using your email.
3. After confirming your email and logging in, go to the "Developers" section or "API Keys" page.
4. Copy your API key. You will use it in the `X-Api-Key` header in your Python requests.

---

## Task 1: Make Your First GET Request

**Goal:** Use the `requests` library to make a simple GET request to the Randommer API.

**Instructions:**
- Install the `requests` library if you haven’t: `pip install requests`
- Send a GET request to the endpoint: `https://randommer.io/api/Card`
- Include your API key in the headers as follows:  
  `"X-Api-Key": "<YOUR_API_KEY>"`
- Print the response JSON.

**Example Output:**
```
{'type': 'Visa', 'number': '4323-1234-5678-9876', 'expiration': '11/27', 'cvv': '421'}
```

---

## Task 2: Get a Random Name

**Goal:** Use the API to get a random name.

**Instructions:**
- Send a GET request to: `https://randommer.io/api/Name`
- Don’t forget to include the API key in the headers.
- Print the random name you get from the response.

**Example Output:**
```
Madison
```

---

## Task 3: List All Available APIs

**Goal:** Discover what APIs are available on Randommer.

**Instructions:**
- Send a GET request to: `https://randommer.io/api/AvailableEndpoints`
- Use your API key in the headers.
- Print the list of endpoints you receive.

**Example Output:**
```
['api/Name', 'api/Card', 'api/Password', 'api/Address', 'api/Phone', ...]
```

---

## Task 4: Generate a Random Password

**Goal:** Use the API to generate a random password.

**Instructions:**
- Send a GET request to: `https://randommer.io/api/Password`
- Include your API key in the headers.
- Print the password you get from the API.

**Example Output:**
```
Qw3!s7zXl9@
```

---

## Task 5: Error Handling

**Goal:** Practice handling API errors.

**Instructions:**
- Send a GET request using an incorrect or missing API key.
- Catch the error and print a friendly message if the request fails (e.g., 401 Unauthorized).
- Try to print the error message returned by the API.

**Example Output:**
```
Request failed! Status code: 401
Error: {"message":"Invalid API Key"}
```

---

**Happy coding!**