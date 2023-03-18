import time
import requests
import os
import sys

# Define the paths of two sample images
SERVER_URL = ''

parent_dir = os.path.dirname(__file__)
IMG_PATHS = [parent_dir + '/test_cases/images/tench.jpeg', 
             parent_dir + '/test_cases/images/turtle.jpeg']

def test_prediction(img_path):
    # Load the image data
    with open(img_path, 'rb') as f:
        img_data = f.read()

    # Make a request to the server with the image data
    start_time = time.time()
    response = requests.post(SERVER_URL, files={'image': img_data})
    end_time = time.time()

    # Print the predicted class and the time taken for the request
    print(f"Image {img_path}: {response.json()} (Time: {end_time - start_time:.2f}s)")

if __name__ == '__main__':
    # Test individual image predictions
    for img_path in IMG_PATHS:
        test_prediction(img_path)

    # Test custom tests if the flag is passed
    if '--test' in sys.argv:
        # Define your custom tests here
        pass
