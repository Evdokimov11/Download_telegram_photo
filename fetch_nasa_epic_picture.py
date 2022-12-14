import argparse
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

from download_image import download_image


def fetch_nasa_epic_picture(api_key, amount, time):

    url = "https://epic.gsfc.nasa.gov/api/natural"

    payload = {
        "api_key": api_key,
        "date": time,
    }

    response = requests.get(url, params=payload)

    response.raise_for_status()

    payload.pop("date")

    for photo_number, photo_information in enumerate(response.json()):

        if photo_number == amount:
            break

        name_photo = photo_information["image"]

        date_str = photo_information["date"]

        full_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

        short_date_link = full_date.date().strftime("%Y/%m/%d")

        url = f"https://api.nasa.gov/EPIC/archive/natural/{short_date_link}/png/{name_photo}.png"

        path_photo = os.path.join("images", f"nasa_epic_{photo_number}.png")

        download_image(url, path_photo, payload)


if __name__ == "__main__":

    load_dotenv()

    nasa_api_key = os.environ["NASA_API_KEY"]

    parser = argparse.ArgumentParser(description="Программа скачивает фотографии Земли с сайта NASA")

    parser.add_argument("amount", help="Кол-во фотографий для скачивания", type=int, nargs="?", default="7")

    parser.add_argument(
        "-d", "--date", help="Дата фотографий Земли в формате YYYY-MM-DD", nargs="?", default="2022-01-01"
    )

    args = parser.parse_args()

    fetch_nasa_epic_picture(nasa_api_key, args.amount, args.date)
