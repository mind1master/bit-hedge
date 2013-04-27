import sys
from utils import proj


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bit_hedge',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
        }
}

if 'test' in sys.argv:
    DATABASES['default']['NAME'] = ':memory:'

SITE_ID = 1

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
USE_TZ = True

USE_I18N = True
USE_L10N = True

SECRET_KEY = 'f3=dg%b600m5aivknk-tld04ucg0a1yj&amp;4+1nxj#a!p3m6kkbp'

ROOT_URLCONF = 'bit_hedge.urls'

WSGI_APPLICATION = 'bit_hedge.wsgi.application'

