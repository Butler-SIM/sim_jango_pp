from .base import *

SECRET_KEY = 'django-insecure-t_9znj@bw+-cbx2nkdwlbihf3woilscsbm+t!=ze$5!sqp3=5w'
algorithm='HS256'
DEBUG = False
ALLOWED_HOSTS = ['*']
#
#DB
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('APP_DB_ENGINE'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        }
     }
