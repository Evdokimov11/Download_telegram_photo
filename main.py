import os
import argparse

from dotenv import load_dotenv
from download_to_telegram import download_to_telegram
from download_image import download_image
from fetch_nasa_epic_picture import fetch_nasa_epic_picture
from fetch_spacex_images import fetch_spacex_images
from fetch_nasa_planetary_apod_picture import fetch_nasa_planetary_apod_picture


if __name__ == '__main__':

    load_dotenv()

    nasa_api_key = os.environ['NASA_API_KEY']

    telegram_bot_api_key = os.environ['TELEGRAM_BOT_API_KEY']
  
    parser = argparse.ArgumentParser(
        description='Программа скачивает фотографии космоса из интернета и отпраляет их в телеграм-канал'
    )

    parser.add_argument('id', help='ID запуска spacex', nargs='?', default='latest')
  
    parser.add_argument('-t', '--time', help='Частота публикации фотографий (указать в часах)', nargs='?', default=4)

    args = parser.parse_args()

    fetch_spacex_images(args.id)
  
    fetch_nasa_planetary_apod_picture(nasa_api_key)    
  
    fetch_nasa_epic_picture(nasa_api_key)

    download_to_telegram(args.time, telegram_bot_api_key)

   
      
 