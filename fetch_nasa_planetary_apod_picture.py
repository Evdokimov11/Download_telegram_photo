import requests
import os
import argparse

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

    photos_information = response.json()

    filtered_information = [dictionary for dictionary in photos_information if 
                                  dictionary['media_type'] != 'other' and 
                                  find_image_format(dictionary['url'])]
  
    for photo_number, photo_information in enumerate(filtered_information):

            photo_link = photo_information['url']
            
            formatted_image = find_image_format(photo_link)
            
            photo_path = os.path.join('images', f'nasa_apod_{photo_number}{formatted_image}')
            
            download_image(photo_link, photo_path)
          

if __name__ == '__main__':

    load_dotenv()
 
    nasa_api_key = os.environ['NASA_API_KEY']
    
    parser = argparse.ArgumentParser(
        description='Программа скачивает фотографии космоса с сайта NASA'
    )

    parser.add_argument('amount', help='Кол-во фотографий для скачивания', nargs='?', default='45')

    args = parser.parse_args()
  
    fetch_nasa_planetary_apod_picture(nasa_api_key, args.amount)    
  