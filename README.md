#批文

```
(sudo )pip install -r requirements.txt
```

```
python manage.py createsuperuser
```

```
python manage.py makemigrations
python manage.py migrate
```

```
celery -A healthdaily worker --loglevel==info
```

```
python manage.py runserver
```
然后访问 localhost:8000
