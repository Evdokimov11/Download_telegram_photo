import os
import telegram

def download_to_telegram():

    telegram_bot_api_key = os.environ['TELEGRAM_BOT_API_KEY']

    bot = telegram.Bot(token=telegram_bot_api_key)

    bot.send_document(chat_id='@space_beautiful_photos', document=open('images/nasa_apod_0.gif', 'rb'))