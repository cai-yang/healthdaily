#批文

安装所需的包
```
(sudo )pip install -r requirements.txt
```

建立管理员
```
python manage.py createsuperuser
```

初始化数据库
```
python manage.py makemigrations
python manage.py migrate
```

需要先运行```(sudo )rabbitmq-server```，<a href='http://www.rabbitmq.com/'>安装rabbitmq</a>

运行任务队列
```
celery -A healthdaily worker --loglevel==info
```

运行
```
python manage.py runserver
```

然后访问 localhost:8000
