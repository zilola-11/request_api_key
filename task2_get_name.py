import requests
import pprint
API_KEY = "e26e5578caae46b4b0a194dc7623ed90"

def get_random_name():
    url = "https://randommer.io/api/Name"
    headers = {
        "X-Api-Key": API_KEY
    }
    response = requests.get(url, headers = headers)
    
    print(response.status_code)
    pprint.pprint(response.json())
    
get_random_name()
"""
    Make a GET request to the Randommer API to get a random name.

    This function should:
    - Send a GET request to: https://randommer.io/api/Name
    - Include the API key in the X-Api-Key header
    - Print the random name from the response
    """
    