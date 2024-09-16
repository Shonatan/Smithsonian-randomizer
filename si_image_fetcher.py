import requests
import random

# Function to get random image media URL from Smithsonian API
def get_random_image():
    url = 'https://api.si.edu/openaccess/api/v1.0/search'
    params = {
        'api_key': 'Os73S8RAyylskTqIKvcmaerE9gNtYDTp9vbTcKKz',
        'q': 'mask',
        'rows': 10,
        'start': random.randint(0, 100)
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Return the first media URL found
    try:
        return data['response']['docs'][0]['online_media']['media'][0]['content']
    except (KeyError, IndexError):
        return "No media found."

# Main script
if __name__ == "__main__":
    media_url = get_random_image()
    print(f"Media URL: {media_url}")
