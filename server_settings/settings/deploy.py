from .base import *


DEBUG = False
ALLOWED_HOSTS = ['*']

print(os.environ.get('APP_DB_ENGINE'))
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
