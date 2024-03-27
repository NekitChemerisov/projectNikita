запуск в venv в window, если нет прав 
Set-ExecutionPolicy Unrestricted -Scope Process

запускаем venv
.venv\Scripts\activate
django-admin startproject nikproject

запуск преокта на django
пускуем с директории
python manage.py runserver

стоп venv
deactivate
