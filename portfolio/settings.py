"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

INTERNAL_IPS = ['127.0.0.1']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'apps.PortfolioAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_ckeditor_5',
    'rosetta',
    'core.apps.CoreConfig',
    'debug_toolbar',
    'django_ratelimit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'core.context_processors.copy_email',
                'core.context_processors.context_data',
                'core.context_processors.context_photo',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]



MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|',
            'bold', 'italic', 'underline', '|',
            'fontSize', 'fontColor', 'fontBackgroundColor', '|',
            'bulletedList',  '|',
            'undo', 'redo'
        ],
         'fontSize': {
            'options': [
                '8px', '12px', '13px', '15px', 'default', '16px', '20px', '24px', 
            ],
            'supportAllValues': True  # Pozwala na pełną elastyczność, jeśli chcesz wpisać rozmiar ręcznie
        },
         'fontColor': {
            'supportCustomColors': True, # Umożliwia wybór dowolnego koloru
             'colors': [
                {
                    'color': '#4770FF',  # primary(like var(--primary) in style.css)
                    'label': 'Primary'
                },
                {
                    'color': '#6c757d',  # Bootstrap secondary
                    'label': 'Secondary'
                },
                {
                    'color': '#198754',  # Bootstrap success
                    'label': 'Success'
                },
                {
                    'color': '#dc3545',  # Bootstrap danger
                    'label': 'Danger'
                },
                {
                    'color': '#ffc107',  # Bootstrap warning
                    'label': 'Warning'
                },
                {
                    'color': '#212529',  # Bootstrap dark
                    'label': 'Dark'
                },
            ]  
        },
        'fontBackgroundColor': {
            'supportCustomColors': True,  # Umożliwia wybór dowolnego koloru tła
        },
        'height': 250,
        'width': '60%',
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3', '|', 'undo', 'redo'
        ],
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/",
        'toolbar': 'full',
        'fontSize_sizes': '10px/10px;12px/12px;14px/14px;16px/16px;18px/18px;',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            'TIMEOUT': 300,
        }
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True,
}