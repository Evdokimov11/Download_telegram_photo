import requests
import os
import argparse

from pprint import pprint
from dotenv import load_dotenv
from download_image import download_image
from urllib.parse import urlparse

def find_image_format(url):

    divided_url = urlparse(url)
  
    path_url = divided_url.path
  
    root_ext = os.path.splitext(path_url)
  
    return root_ext[1]



def fetch_nasa_planetary_apod_picture(api_key, amount):

    url = 'https://api.nasa.gov/planetary/apod'
    
    payload = {
        'api_key': api_key,
        'count' : amount,       
    }

    response = requests.get(url, params=payload)

    response.raise_for_status()

    nasa_photos_information = response.json()

    filtered_photos_information = [dict for dict in nasa_photos_information if 
                                  dict['media_type'] != 'other' and 
                                  find_image_format(dict['url'])]
  
    for nasa_photo_number, nasa_photo_information in enumerate(filtered_photos_information):

            nasa_photo_link = nasa_photo_information['url']
            
            formated_image = find_image_format(nasa_photo_link)
            
            photo_path = os.path.join('images', f'nasa_apod_{nasa_photo_number}{formated_image}')
            
            download_image(nasa_photo_link, photo_path)
          

if __name__ == '__main__':

    load_dotenv()
 
    nasa_api_key = os.environ['NASA_API_KEY']
    
    parser = argparse.ArgumentParser(
        description='Программа скачивает фотографии космоса с сайта NASA'
    )

    parser.add_argument('amount', help='Кол-во фотографий для скачивания', nargs='?', default='45')

    args = parser.parse_args()
  
    fetch_nasa_planetary_apod_picture(nasa_api_key, args.amount)    
  