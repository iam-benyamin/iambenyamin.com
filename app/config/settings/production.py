from config.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'iambenyamin.com',
    'www.iambenyamin.com',
    'mail.iambenyamin.com',
]


# database config for postgreql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'iambeny1_db',
        'USER': 'iambeny1_user',
        'PASSWORD': 'ShmH}xpM9)[^',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


TIME_ZONE = 'Asia/Tehran'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = '/home/iambeny1/public_html/iambenyamin.com/static/'
MEDIA_ROOT = '/home/iambeny1/public_html/iambenyamin.com/media/'
