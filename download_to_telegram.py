import os
import telegram
import random
import argparse

from dotenv import load_dotenv


def download_to_telegram(telegram_bot_api_key, photo_path):

    bot = telegram.Bot(token=telegram_bot_api_key)
  
    if photo_path: 
              
        bot.send_photo(chat_id='@space_beautiful_photos', photo=open(photo_path, 'rb'))

    else:
      
        names_photos = []
    
        for address, dirs, files in os.walk('images'):
        
            for name in files:
      
                names_photos.append(name)


        random_photo = random.choice(names_photos)
       
        bot.send_photo(chat_id='@space_beautiful_photos', photo=open(f'images/{random_photo}','rb'))

    
if __name__ == '__main__':

    load_dotenv()
  
    telegram_bot_api_key = os.environ['TELEGRAM_BOT_API_KEY']
  
    parser = argparse.ArgumentParser(
        description='Программа публикует картинки из в канал телеграм-канал.')

    parser.add_argument('-p', '--path', help='Путь к файлу для скачивания')

    args = parser.parse_args()

    stats = os.stat(args.path)
                
    if stats.st_size > 20000000:
    
        print("File size is too big, please reduce it")
        
    else:
            
        download_to_telegram(telegram_bot_api_key, args.path)
    
  
 



      
    