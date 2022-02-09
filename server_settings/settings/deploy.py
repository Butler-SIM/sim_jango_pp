from .base import *


DEBUG = False
ALLOWED_HOSTS = ['*']

print(os.environ.get('APP_DB_ENGINE'))
#
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
