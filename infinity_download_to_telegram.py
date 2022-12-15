import os
import random
import time
import argparse

from download_to_telegram import download_to_telegram
from dotenv import load_dotenv


def infinity_download_to_telegram(frequency_publish, telegram_bot_api_key): 

    names_photos = []
    
    for address, dirs, files in os.walk('images'):
        
        for name in files:
      
            names_photos.append(name)

        while True :

            random.shuffle(names_photos)
      
            for name_photo in names_photos:
        
                stats = os.stat(f'images/{name_photo}')
              
                if stats.st_size > 20000000:
    
                    continue
              
                download_to_telegram(telegram_bot_api_key, f'images/{name_photo}')
    
                time.sleep(3600*frequency_publish)


if __name__ == '__main__':

    load_dotenv()

    telegram_bot_api_key = os.environ['TELEGRAM_BOT_API_KEY']
  
    parser = argparse.ArgumentParser(
        description='Программа запускает бесконечный цикл для отправки фото в телеграм-канал.')
    
    parser.add_argument('-f', '--frequency_publish', help='Частота публикации фотографий (указать в часах)', type=int, nargs='?', default=4)

    args = parser.parse_args()
                        
    download_to_telegram(telegram_bot_api_key, args.frequency_publish)
      