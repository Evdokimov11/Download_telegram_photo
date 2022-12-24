import requests
import argparse
import os

from download_image import download_image


def fetch_spacex_images(launch_id):

    url = f'https://api.spacexdata.com/v5/launches/{launch_id}' 

    response = requests.get(url)

    response.raise_for_status()

    spacex_photo_links = response.json()['links']['flickr']['original']

    for photo_link_number, spacex_photo_link in enumerate(spacex_photo_links):
        
         photo_path = os.path.join('images', f'spacex_{photo_link_number}.jpg')

         download_image(spacex_photo_link, photo_path)
    
     
if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Программа скачивает фотографии с сайта spacex'
    )

    parser.add_argument('launch_id', help='ID запуска', nargs='?', default='latest')

    args = parser.parse_args()
    
    fetch_spacex_images(args.launch_id)
