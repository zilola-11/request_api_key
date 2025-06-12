import requests

API_KEY = "e26e5578caae46b4b0a194dc7623ed90"


def generate_random_password():
    url = "https://randommer.io/api/Password"
    headers = {
        "X-Api-Key": API_KEY
    }
    response = requests.get(url, headers = headers)
    
    print(response.text)

generate_random_password()
"""
Make a GET request to the Randommer API to generate a random password.

This function should:
- Send a GET request to: https://randommer.io/api/Password
- Include the API key in the X-Api-Key header
- Print the generated password from the response
"""