import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '$+x-4c045-u16r&6&7p#565i#*xjgrlp@lxe-=0c&&chwiriof'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '64.227.71.171']

STATIC_ROOT = '/home/django/django_project/django_project/static'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'quiz',
        'USER': 'userdb',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}