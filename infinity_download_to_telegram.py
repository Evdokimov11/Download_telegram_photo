import os
import random
import time
import argparse

from download_to_telegram import download_to_telegram
from dotenv import load_dotenv
from get_names_photos import get_names_photos


def infinity_download_to_telegram(telegram_bot_api_key, frequency_publish, chat_id): 

    names_photos = get_names_photos()
    
    while True :

        random.shuffle(names_photos)
      
        for name_photo in names_photos:
            
            path_photo = os.path.join('images', name_photo)
              
            download_to_telegram(telegram_bot_api_key, path_photo, chat_id)
                 
            time.sleep(3600*frequency_publish)


if __name__ == '__main__':

    load_dotenv()

    telegram_bot_api_key = os.environ['TELEGRAM_BOT_API_KEY']
  
    parser = argparse.ArgumentParser(
        description='Программа запускает бесконечный цикл для отправки фото в телеграм-канал.')
    
    parser.add_argument('-f', '--frequency_publish', help='Частота публикации фотографий (указать в часах)', type=int, nargs='?', default=4)
    
    parser.add_argument('-c', '--chat_id', help='Айди чата в формате @chat_id')

    args = parser.parse_args()
                        
    infinity_download_to_telegram(telegram_bot_api_key, args.frequency_publish, args.chat_id)
      