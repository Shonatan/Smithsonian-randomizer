import requests
from PIL import Image
from io import BytesIO
import random

# Function to get random image from Smithsonian API
def get_random_image():
    url = 'https://api.si.edu/openaccess/api/v1.0/search'
    params = {
        'api_key': 'Os73S8RAyylskTqIKvcmaerE9gNtYDTp9vbTcKKz',  # Replace with your actual API key
        'q': 'art',  # Search query, e.g., 'art'
        'rows': 10,  # Number of results to fetch
        'start': random.randint(0, 100)  # Random start index for pagination
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    # Get a random image URL from the results
    items = data['response']['docs']
    if items:
        image_url = random.choice(items)['media'][0]['url']
        return image_url
    return None

# Function to display the image
def display_image(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.show()

# Main script
if __name__ == "__main__":
    image_url = get_random_image()
    if image_url:
        display_image(image_url)
    else:
        print("No images found.")
