"""
Django settings for healthdaily project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z8&8lhd7)kj=)-ivs12)g87)b9*jj_-ah$2j#*7yej_vm%&n$)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ribao',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'healthdaily.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

"""
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
    )
}
"""

WSGI_APPLICATION = 'healthdaily.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
#-------this is for the sae environ-------
"""
if 'SERVER_SOFTWARE' in os.environ:
    # SAE
    import sae.const
    db_name = sae.const.MYSQL_DB
    name = sae.const.MYSQL_USER
    pwd = sae.const.MYSQL_PASS
    host = sae.const.MYSQL_HOST
    port = sae.const.MYSQL_PORT
    host_s = sae.const.MYSQL_HOST_S
else:
    # local
    db_name ="mytestdb"
    name ="root"
    pwd ="7127"
    host ="127.0.0.1"
    port ="3306"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_name,					  # Or path to database file if using sqlite3.
        'USER': name,					  # Not used with sqlite3.
        'PASSWORD': pwd,				  # Not used with sqlite3.
        'HOST': host,					  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': port,					  # Set to empty string for default. Not used with sqlite3.
    }
}
"""
#-------------this is for postgresql, change the settings to your own

db_name ="testdb"
name ="yc"
pwd ="ubuntu"
host ="127.0.0.1"
port ="5432"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': db_name,
        'USER': name,
        'PASSWORD': pwd,
        'HOST': host,
        'PORT': port,
    }
}
"""
#for test, use sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = 'ribao/static/'

STATIC_URL = '/static/'
