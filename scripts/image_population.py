import os
import requests
from dotenv import load_dotenv


load_dotenv()

api_upload_url = os.getenv("API_UPLOAD_URL")

directory = ""
all_images = []

for image in os.listdir(directory):
    image_path = os.path.join(directory, image)
    if os.path.isfile(image_path):
        print("Image:", image_path)
        with open(image_path, 'rb') as file:
            response = requests.post(api_upload_url, files={'file': file})
            print(response.content)
            if response.status_code == 200:
                link = response.json().get('url', None)
                if link:
                    all_images.append(link)

print(all_images)

# Write the image links to a file
with open('links.txt', 'w') as file:
    for idx, image_link in enumerate(all_images):
        file.write(f'Listing {idx+1}:\n')
        file.write(f'{image_link}\n')
