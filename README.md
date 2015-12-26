
##Celery Integration
To run the asynchronous task in the background
install the following packages in your virtualenv
```
$ pip install celery
$ pip install redis
```

to use the redis as a message broker between the celery worker, install redis-server
```
$ sudo apt-get install redis-server
```

To integrate with django, django-celery library must installed

```
$ pip install django-celery
```
add `djcelery` library to your INSTALLED_APPS

migrate your database

```
$ ./manage.py makemigrations djcelery
$ ./manage.py migrate djcelery
```

to save the result provide by the celery workers in django db,  just need to add

```
app.conf.update(
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
)
```

to `settings.py` file of your django project

