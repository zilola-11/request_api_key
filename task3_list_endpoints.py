import requests

API_KEY = "e26e5578caae46b4b0a194dc7623ed90"

def list_available_endpoints():
    
    url = "https://randommer.io/api/AvailableEndpoints"
    
    headers = {
        "X-Api_Key": API_KEY
    }
    try:
        response = requests.get(url, headers=headers)
        response.status_code()
        data = response.json()
    
    print("Available Endpoints:")
    for endpoint in data:
        print(f"-{endpoint}")
    except:
        
list_available_endpoints()
"""
    Make a GET request to discover all available endpoints on Randommer API.

    This function should:
    - Send a GET request to: https://randommer.io/api/AvailableEndpoints
    - Include the API key in the X-Api-Key header
    - Print the list of available endpoints from the response
    """
