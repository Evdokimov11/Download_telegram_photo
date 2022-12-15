import requests
import os

from dotenv import load_dotenv
from download_image import download_image
from urllib.parse import urlparse
from datetime import datetime

def fetch_nasa_epic_picture(api_key):
  
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

    fetch_nasa_epic_picture(my_secret)
  