import requests

API_KEY = "e26e5578caae46b4b0a194dc7623ed90"

import pprint
def get_random_card():
    url = "https://randommer.io/api/Card"
    headers = {
        "X-Api-Key": API_KEY
        }
    response = requests.get(url, headers=headers)
    pprint.pprint(response.text)
    
get_random_card()
    
    
        
"""
    Make a GET request to the Randommer API to get a random card.

    This function should:
    - Send a GET request to: https://randommer.io/api/Card
    - Include the API key in the X-Api-Key header
    - Print the response JSON containing card information
    """
