import os

from dotenv import load_dotenv
from download_to_telegram import download_to_telegram
from download_image import download_image
from fetch_nasa_epic_picture import fetch_nasa_epic_picture
from fetch_spacex_images import fetch_spacex_images
from fetch_nasa_planetary_apod_picture import fetch_nasa_planetary_apod_picture


if __name__ == '__main__':

    load_dotenv()

    my_secret = os.environ['NASA_API_KEY']

    fetch_spacex_images('latest')
  
    fetch_nasa_planetary_apod_picture(my_secret)    
  
    fetch_nasa_epic_picture(my_secret)

    download_to_telegram()

   
      
 