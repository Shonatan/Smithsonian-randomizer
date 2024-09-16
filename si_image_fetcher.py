import requests
import json  # Import json module for pretty-printing

# Test the API key and print the response neatly
def test_api_key():
    url = 'https://api.si.edu/openaccess/api/v1.0/search'
    params = {
        'api_key': 'Os73S8RAyylskTqIKvcmaerE9gNtYDTp9vbTcKKz',
        'q': 'art',  # Example query
        'rows': 1  # Limit to 1 result for simplicity
    }
    response = requests.get(url, params=params)
    
    # Pretty-print the JSON response
    if response.status_code == 200:
        print("API Key is working!")
        print(json.dumps(response.json(), indent=4))  # Pretty-print the response
    else:
        print(f"Failed to connect: {response.status_code}")

if __name__ == "__main__":
    test_api_key()
