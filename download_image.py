import argparse
import os
from pathlib import Path
from urllib.parse import urlparse

import requests


def download_image(url, file_path, payload=None):

    divided_url = urlparse(file_path)

    path_url = divided_url.path

    file_path_name = os.path.split(path_url)

    response = requests.get(url, params=payload)

    response.raise_for_status()

    Path(file_path_name[0]).mkdir(parents=True, exist_ok=True)

    with open(file_path, "wb") as file:

        file.write(response.content)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Программа скачивает фотографии по ссылке")

    parser.add_argument("link", help="ссылка на фото")

    parser.add_argument("-p", "--path", help="Путь к файлу для скачивания")

    args = parser.parse_args()

    download_image(args.link, args.path)
