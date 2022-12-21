import os
import argparse


from dotenv import load_dotenv
from infinity_download_to_telegram import infinity_download_to_telegram
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

    parser.add_argument('launch_id', help='ID запуска spacex', nargs='?', default='latest')

    parser.add_argument('-f', '--frequency_publish', help='Частота публикации фотографий (указать в часах)', type=int, nargs='?', default=4)
    
    parser.add_argument('-s', '--space_photo_amount', help='Кол-во фотографий для скачивания фотографий космоса', type=int, nargs='?', default=45)
    
    parser.add_argument('-e', '--earth_photo_amount', help='Кол-во фотографий для скачивания фотографий Земли', type=int, nargs='?', default=7)
    
    parser.add_argument('-d', '--date', help='Дата фотографий Земли в формате YYYY-MM-DD', nargs='?', default='2022-01-01')
    
    parser.add_argument('-c', '--chat_id', help='Айди чата в формате @chat_id')

    args = parser.parse_args()

    #fetch_spacex_images(args.launch_id)
  
    #fetch_nasa_planetary_apod_picture(nasa_api_key, args.space_photo_amount)    
  
    #fetch_nasa_epic_picture(nasa_api_key, args.earth_photo_amount, args.date)
    
    infinity_download_to_telegram(telegram_bot_api_key, args.frequency_publish, args.chat_id)
    

    

            

   
      
 