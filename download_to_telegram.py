import os
import telegram
import random
import argparse

from dotenv import load_dotenv
from scripts import get_names_photos
from scripts import send_to_telegram



def download_to_telegram(telegram_bot_api_key, photo_path, chat_id):

    bot = telegram.Bot(token=telegram_bot_api_key)
  
    if photo_path: 
              
        send_to_telegram(photo_path, chat_id, bot)

    else:
    
        names_photos = get_names_photos()

        random_photo = random.choice(names_photos)
        
        rand_photo_path = os.path.join('images', random_photo)
        
        send_to_telegram(rand_photo_path, chat_id, bot)

    
if __name__ == '__main__':

    load_dotenv()
  
    telegram_bot_api_key = os.environ['TELEGRAM_BOT_API_KEY']
  
    parser = argparse.ArgumentParser(
        description='Программа публикует картинки из в канал телеграм-канал.')

    parser.add_argument('-p', '--path', help='Путь к файлу для скачивания', nargs='?', default='')
    
    parser.add_argument('-c', '--chat_id', help='Айди чата в формате @chat_id')

    args = parser.parse_args()

    download_to_telegram(telegram_bot_api_key, args.path, args.chat_id)
    
  
 



      
    