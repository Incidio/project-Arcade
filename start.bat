@echo off
start http://127.0.0.1:8000
call .\venv\Scripts\activate
python manage.py runserver