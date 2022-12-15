import requests
import os

from download_image import download_image
from urllib.parse import urlparse
from dotenv import load_dotenv

def find_image_format(url):

    divided_url = urlparse(url)
  
    path_url = divided_url.path
  
    root_ext = os.path.splitext(path_url)
  
    return root_ext[1]



def fetch_nasa_planetary_apod_picture(api_key):

    url = 'https://api.nasa.gov/planetary/apod'
    
    payload = {
        'api_key': api_key,
        'count' : 45,       
    }

    response = requests.get(url, params=payload)

    response.raise_for_status()

    nasa_photos_information = response.json()

    not_photo_count = 0
  
    for nasa_photo_information_number, nasa_photo_information in enumerate(nasa_photos_information):
      
        link_nasa_photo = nasa_photo_information['url']

        image_formated = find_image_format(link_nasa_photo)
       
        if image_formated :

            hd_link_nasa_photo = nasa_photo_information['url']
            
            download_image(hd_link_nasa_photo, f"images/nasa_apod_{nasa_photo_information_number-not_photo_count}{image_formated}")
          
        else:
          
            not_photo_count = not_photo_count + 1

if __name__ == '__main__':

    load_dotenv()

    nasa_api_key = os.environ['NASA_API_KEY']
  
    fetch_nasa_planetary_apod_picture(nasa_api_key)    
  