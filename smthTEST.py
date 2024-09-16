import requests

# Test the API key by making a simple request
def test_api_key():
    url = 'https://api.si.edu/openaccess/api/v1.0/search'
    params = {
        'api_key': 'Os73S8RAyylskTqIKvcmaerE9gNtYDTp9vbTcKKz',
        'q': 'art',  # Example query
        'rows': 1  # Limit to 1 result for simplicity
    }
    response = requests.get(url, params=params)
    
    # Print status and part of the response
    if response.status_code == 200:
        print("API Key is working!")
        print(response.json())
    else:
        print(f"Failed to connect: {response.status_code}")

if __name__ == "__main__":
    test_api_key()
