import os
import telegram
import time
import random
import argparse

from dotenv import load_dotenv


def download_to_telegram(frequency_publish, telegram_bot_api_key):

    bot = telegram.Bot(token=telegram_bot_api_key)

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
              
            bot.send_photo(chat_id='@space_beautiful_photos', photo=open(f'images/{name_photo}', 'rb'))
    
            time.sleep(3600*frequency_publish)


if __name__ == '__main__':

    load_dotenv()

    telegram_bot_api_key = os.environ['TELEGRAM_BOT_API_KEY']
  
    parser = argparse.ArgumentParser(
        description='Программа публикует картинки из в канал телеграм-канал.')
    

    parser.add_argument('frequency_publish', help='Частота публикации фотографий (указать в часах)', nargs='?', default=4)

    args = parser.parse_args()
    
    download_to_telegram(args.frequency_publish, telegram_bot_api_key)
    
  
 



      
    