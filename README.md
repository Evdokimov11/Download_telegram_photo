### Загрузка фотографий космоса в телеграм с помощью телеграм-бота

Данный проект создан для скачивания фотографий с сайтов NASA и Spacex, с последующей их загрузкой в телеграм с помощью телеграм-бота 

Для работы с программой вам необходимо запустить файл ```main.py```. 

Ниже описаны функции и пример запуска каждого скрипта. 


## main.py

Для запуска программы: 

```
python main.py
```
Во время выполнения программы в консоль будет выводиться путь фотографии в вашей локальной системе.

Пример запуска программы представлен ниже

![2022-12-15_04-02-47](https://user-images.githubusercontent.com/42433463/207741472-b11187dc-4921-4ba8-b389-f59c8dea393b.png)

Также вы можете передать в файл ```main.py``` два аргумента : 

* ID запуска spacex (по умолчанию - последний запуск);

* Используя ключ -f можно задать частоту отправки фотографий(указать кол-во часов) в телеграм-канал(по умолчанию - 4 часа).

Для запуска программы с параметрами необходимо выполнить команду: 

```
python main.py python main.py ID_ЗАПУСКА -f КОЛИЧЕСТВО_ЧАСОВ
```
Пример запуска с параметрами представлен ниже:

![2022-12-15_12-05-47](https://user-images.githubusercontent.com/42433463/207805804-92b95ecc-c81f-46fd-adac-323bd0bc2534.png)


##download_image.py

Данный скрипт используется для загрузки фотографии по ссылке.

Для запуска программы вам необходимо передать два параметра:

* Ссылка на фото

* Используя ключ -p необходимо передать путь файлу для скачивания

Для запуска программы с параметрами необходимо выполнить команду: 

```
python download_image.py CСЫЛКА_НА_ФОТО -p ПУТЬ_ДЛЯ_СКАЧИВАНИЯ
```
Пример запуска с параметрами представлен ниже:

![2022-12-15_12-23-45](https://user-images.githubusercontent.com/42433463/207809458-cc8a7df9-476e-4e10-93ac-62e8944bf09a.png)


##fetch_spacex_images.py

Данный скрипт используется для загрузки фотографий запуска spacex.

Для запуска программы вам необходимо передать id запуска, по умолчанию скачаются фотографии последнего запуска

Для запуска программы с параметрами необходимо выполнить команду: 

```
python fetch_spacex_images.py ID_ЗАПУСКА
```
Пример запуска с параметрами представлен ниже:

![2022-12-15_12-29-41](https://user-images.githubusercontent.com/42433463/207810475-c6684529-d94b-4ec0-b842-e28a52905b2b.png)


##fetch_nasa_planetary_apod_picture.py

Данный скрипт используется для загрузки фотографий c сайта NASA.

Для запуска программы необходимо выполнить команду: 

```
python fetch_nasa_planetary_apod_picture.py
```
Пример запуска с параметрами представлен ниже:

![2022-12-15_12-38-02](https://user-images.githubusercontent.com/42433463/207812158-b611fa93-ab1e-4192-8899-a9ef416310fd.png)


##fetch_nasa_planetary_apod_picture.py

Данный скрипт используется для загрузки фотографий нашей планеты c сайта NASA.

Для запуска программы необходимо выполнить команду: 

```
python fetch_nasa_epic_picture.py
```
Пример запуска с параметрами представлен ниже:

![2022-12-15_12-41-16](https://user-images.githubusercontent.com/42433463/207812905-2bd7d66f-3dd6-4e0a-b3a1-6b118c63f05f.png)


##download_to_telegram.py

Данный скрипт используется для отправления фотографии в телеграм канал.

Для запуска программы вам необходимо передать путь к файлу для отправления с помощью ключа -p, иначе скрипт выберет любую из фотографий

Для запуска программы с параметрами необходимо выполнить команду: 

```
python download_to_telegram.py -p ПУТЬ_ДО_ФАЙЛА  
```
Пример запуска с параметрами представлен ниже:

![2022-12-15_12-47-54](https://user-images.githubusercontent.com/42433463/207814260-558765a8-3e1d-4c49-9606-521975e1d367.png)


##infinity_download_to_telegram.py

Данный скрипт используется для запуска бесконечного цикла отправления фотографий в телеграм.

В случае если все фото из списка будут отправлены программа перемешает их случайным образом и начнет заново.

Для запуска программы вам необходимо передать частоту к файлу отправления(указать кол-во часов) с помощью ключа -p, иначе программа установит интервал в 4 часа

Для запуска программы с параметрами необходимо выполнить команду: 

```
python infinity_download_to_telegram.py -f ЧИСЛО_ЧАСОВ_ДЛЯ_ИНТЕРВАЛА 
```
Пример запуска с параметрами представлен ниже:

![2022-12-15_12-52-26](https://user-images.githubusercontent.com/42433463/207815231-030cd718-bb0e-4bad-bee6-28446a723e43.png)


### Как установить

Для корректной работы программы вам необходимо создать файл .env и записать в него ваш API-ключ полученный на сайте [NASA](https://api.nasa.gov/#signUp) в следующем формате: ```NASA_API_KEY=Ваш_API_ключ```

Python3 должен быть уже установлен. 

Также вам необходимо установить соответствующие внешние пакеты. Версии данных пакетов вы можете найти в файле requirements.txt

Используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
