import os
from pathlib import Path
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
INTERNAL_IPS = ['127.0.0.1']
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'modeltranslation',
    'rosetta',

    'apps.PortfolioAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_ckeditor_5',
    'core.apps.CoreConfig',
    'debug_toolbar',
    'django_ratelimit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
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
                'core.context_processors.context_personal_info',
                'core.context_processors.context_photo',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'
MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True
USE_L10N = True

USE_TZ = True # time zone



LANGUAGES = (
    ('en', _('English')),
    ('pl', _('Polish')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

STATIC_URL = '/static/'

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
