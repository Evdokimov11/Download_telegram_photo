import os
import telegram

def download_to_telegram():

    telegram_bot_api_key = os.environ['TELEGRAM_BOT_API_KEY']

    bot = telegram.Bot(token=telegram_bot_api_key)

    bot.send_message(chat_id='@space_beautiful_photos', text='Hi John!')
  