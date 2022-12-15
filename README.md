# fabrique_test_task

### Тестовое задание для Фабрики решений 

## Для запуска проекта необходимо:
1. Скопировать git@github.com:DarkSou1/fabrique_test_task.git
```commandline
git@github.com:DarkSou1/fabrique_test_task.git
```
2. Выполнить команду 
```commandline
git clone git@github.com:DarkSou1/fabrique_test_task.git
```
3. Установить и активировать виртуальное окружение
```
python -m venv env
```
```
source env/bin/activate
```
```
python -m pip install --upgrade pip
```
4. Создать суперпользователя для доступа к админстрированию проекта.
```commandline
python manage.py createsuperuser
```

5. Перейти в терминал, установить файл с зависимостями
```commandline
pip install -r requirements.txt 
```
6. Перейти в папку с проектом (где расположен файл manage.py)
7. Выполнить миграции командами: 
```commandline
python manage.py makemigrations
python manage.py migrate 
```
8. Запустить проект
```commandline
python manage.py runserver
```
### В проекте доступны следующие эндпоинты 
- Пользователи        http://127.0.0.1:8000/api/v1/client/
```
{ "id": "int",
 "phone_nunmer": "string",
 "tag": "string", 
 "timezone": "string",
}
```
- Рассылки     http://127.0.0.1:8000/api/v1/distribution/
```
{ "id": "int",
 "date_time_start": "%d.%m.%Y %H:%M",
 "text": "string", 
 "filter": "string",
 "data_time_finish": "%d.%m.%Y %H:%M",
}
```
- Cообщения http://127.0.0.1:8000/api/v1/message/


![](https://img.shields.io/pypi/pyversions/p5?logo=python&logoColor=yellow&style=for-the-badge)
![](https://img.shields.io/badge/Django-3.2.15-blue)
![](https://img.shields.io/badge/DRF-3.14.0-lightblue)