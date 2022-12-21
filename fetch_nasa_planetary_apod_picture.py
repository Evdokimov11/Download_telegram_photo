import requests
import os
from pprint import pprint

from dotenv import load_dotenv
from download_image import download_image
from urllib.parse import urlparse

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
  
    for nasa_photo_number, nasa_photo_information in enumerate(nasa_photos_information):

        if nasa_photo_information['media_type'] == 'other' :

                continue   
        
        nasa_photo_link = nasa_photo_information['url']
      
        image_formated = find_image_format(nasa_photo_link)
       
        if image_formated :

            nasa_hd_photo_link = nasa_photo_information['url']
            
            path_photo = os.path.join('images', f'nasa_apod_{nasa_photo_number-not_photo_count}{image_formated}')
            
            download_image(nasa_hd_photo_link, path_photo)
          
        else:
          
            not_photo_count = not_photo_count + 1

if __name__ == '__main__':

    load_dotenv()
 
    my_secret = os.environ['NASA_API_KEY']
  
    fetch_nasa_planetary_apod_picture(my_secret)    
  