from .base import *

SECRET_KEY = 'django-insecure-t_9znj@bw+-cbx2nkdwlbihf3woilscsbm+t!=ze$5!sqp3=5w'
algorithm='HS256'
DEBUG = True
ALLOWED_HOSTS = ['*']

#DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'butler-sim',
        'USER': 'admin',
        'PASSWORD': 'qwer1234',
        'HOST': 'butlersimdb.cypn7ittsrwd.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
        "OPTIONS": {"charset": "utf8mb4"},
    }
}

