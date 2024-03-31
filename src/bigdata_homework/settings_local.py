from pathlib import Path

# This file contains the settings that are specific to the local environment


# the root directory of the project
SRC_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = SRC_DIR.parent

DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'django-insecure-9xi+45#(0+5v*8uf!2gk6j)o@ml*61cznbi=xzvq($#1g9hjge'

USE_STATICFILES_DIRS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bigdataDB',  # Your database name
        'USER': 'postgreadmin',  # Your database user
        'PASSWORD': 'postgreadmin',  # Your database password
        'HOST': 'db',  # Name of the service defined in docker-compose
        'PORT': '5432',
    }
}