from django.core.management.utils import get_random_secret_key

from config.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# security redirect http to https
SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS = [
    'iambenyamin.com',
    'www.iambenyamin.com',
    'mail.iambenyamin.com',
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_random_secret_key()

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
STATIC_ROOT = '/home/iambeny1/public_html/static/'
MEDIA_ROOT = '/home/iambeny1/public_html/media/'
