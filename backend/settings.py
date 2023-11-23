"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from celery.schedules import timedelta

load_dotenv('.env')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend.api',
    'rest_framework',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'db',
        'PORT': '3306'
    }
}

# Configuration Celery
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL'); # URL de connexion au broker Redis
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND') # URL de connexion pour les résultats des tâches Celery
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

# Configuration pour planifier les tâches avec Celery Beat (optionnel)
CELERY_BEAT_SCHEDULE = {
    'clean-expired-tokens': {
        'task': 'backend.tasks.task.clean_expired_tokens_task',
        # 'schedule': schedules.crontab(minute=0),  # Exécutez la tâche au début de chaque heure
        'schedule': timedelta(seconds=10),  # Exécutez la tâche toute les 10 secondes
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Whitelist localhost:3000 (React port) for CORS
# CORS_ALLOW_ALL_ORIGINS = False  # Désactivez l'autorisation de toutes les origines.
CORS_ALLOW_CREDENTIALS = True # Autorisez les requêtes avec des credentials (cookies, authentification, etc.).

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.permissions.AllowAny',
#     ],
# }


 # Ajoutez ici les origines que vous souhaitez autoriser
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://172.22.0.2:3000"
]

# Par défaut, APPEND_SLASH est défini sur True, ce qui signifie que Django ajoutera
# automatiquement une barre oblique à la fin des URL qui n'en ont pas lors de la redirection.
# Cela est fait pour maintenir la cohérence et la compatibilité avec les pratiques web courantes.
APPEND_SLASH = False

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'api.User'
