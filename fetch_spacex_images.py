import requests
import sys
import argparse

from download_image import download_image

def fetch_spacex_images(id):

    url = f'https://api.spacexdata.com/v5/launches/{id}' 

    response = requests.get(url)

    response.raise_for_status()

    links_spacex_photo = response.json()['links']['flickr']['original']

    for link_spacex_photo_number, link_spacex_photo in enumerate(links_spacex_photo):

         download_image(link_spacex_photo, f"images/spacex_{link_spacex_photo_number}.jpg")
    
     

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Программа скачивает фотографии с сайта spacex'
    )

    parser.add_argument('id', help='ID запуска', nargs='?', default='latest')

    args = parser.parse_args()
    
    fetch_spacex_images(args.id)
    
 
  
 

