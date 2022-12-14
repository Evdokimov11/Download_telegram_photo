import requests
import os
import time

from pprint import pprint
from pathlib import Path
from urllib.parse import urlparse
from datetime import datetime
from dotenv import load_dotenv



def download_image(url, file_path):
  
    print('Downloading photo in :', file_path)
  
    divided_url = urlparse(file_path)
  
    path_url = divided_url.path

    file_path_name = os.path.split(path_url)
  
    response = requests.get(url)
  
    response.raise_for_status()
  
    Path(file_path_name[0]).mkdir(parents=True, exist_ok=True)
  
    with open(file_path, 'wb') as file:
        
        file.write(response.content)
      
        time.sleep(1) #my internet is too slow, so i use 'sleep' to wait'
  
    return


def find_image_format(url):

    divided_url = urlparse(url)
  
    path_url = divided_url.path
  
    root_ext = os.path.splitext(path_url)
  
    return root_ext[1]


def fetch_spacex_last_launch():

    #url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a' link for check

    url = 'https://api.spacexdata.com/v5/launches/latest'

    response = requests.get(url)

    response.raise_for_status()

    links_spacex_photo = response.json()['links']['flickr']['original']

    for link_spacex_photo_number, link_spacex_photo in enumerate(links_spacex_photo):
  
        download_image(link_spacex_photo, f"images/spacex_{link_spacex_photo_number}.jpg")
      
     

def nasa_planetary_apod_picture(api_key):

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

            hd_link_nasa_photo = nasa_photo_information['hdurl']
          
            download_image(hd_link_nasa_photo, f"images/nasa_apod_{nasa_photo_information_number-not_photo_count}{image_formated}")
          
        else:
          
            not_photo_count = not_photo_count + 1


def nasa_epic_picture(api_key):
  
    url = 'https://epic.gsfc.nasa.gov/api/natural'
    
    payload = {
        'api_key': api_key,   
        'date' : '2022-01-01',
    }

    response = requests.get(url, params=payload)

    response.raise_for_status()

    information = []
    
    for nasa_photo_information_number, nasa_photo_information in enumerate(response.json()) :

        if nasa_photo_information_number > 7:
            break

        name_photo = nasa_photo_information ['image']

        date_str = nasa_photo_information['date']
      
        full_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
 
        short_date_link_formated = full_date.date().strftime("%Y/%m/%d")
  
        url = f'https://api.nasa.gov/EPIC/archive/natural/{short_date_link_formated}/png/{name_photo}.png?api_key={api_key}'

        download_image(url, f"images/nasa_epic_{nasa_photo_information_number}.png")

if __name__ == '__main__':

  load_dotenv()
  
  my_secret = os.environ['NASA_API_KEY']

  fetch_spacex_last_launch()
  
  nasa_planetary_apod_picture(my_secret)

  nasa_epic_picture(my_secret)







  













