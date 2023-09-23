from pathlib import Path
import os
from . info import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5szf7n11*5)*z@4$mfbd6*x^#(_r^c(cyqbur*)o^#nf%@8m$7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # 'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'basket',
    'account',
    'orders',
    'mptt',
    "core",
    'checkout',
    'chapa_payment',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'core.urls'

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
                'store.context_processors.categories',
                'basket.context_processors.basket',
            ],
        },
    },
]


# WSGI_APPLICATION = 'application'
# # WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USER_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")


# GOOGLE_API_KEY = "AIzaSyDq6b3Bm8EC9rqyGyGzA3fJ7hFd7BMq6uc"

# # RECAPTCHA_PUBLIC_KEY = "6LdYWMUjAAAAABT4ug-cOumGWagi97UL-CSCaTJ4"

# RECAPTCHA_PRIVATE_KEY = "6LdYWMUjAAAAABbpu982HygZPQxPKnGiHW1b9ysk"


# Basket session ID
BASKET_SESSION_ID = "basket"


# # Custom user model


# LOGIN_URL = "customer:sign-in"
# LOGIN_REDIRECT_URL = "customer:account"
# LOGOUT_REDIRECT_URL = "costomer:sign-in"


# Email setting
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

BASE_COUNTRY = "ET"

AUTH_USER_MODEL = 'account.Customer'
LOGIN_REDIRECT_URL = '/account/dashboard'
LOGIN_URL = '/account/login/'


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


CHAPA_SECRET = "CHASECK_TEST-dcWpiCHYOU4sEBOIz7WPmWzjN7tjqg5L"
CHAPA_PUBLIC_KEY = 'CHAPUBK_TEST-EdQ9zt1Qmh7pU96NQPwxqXntllv9oSei'
CHAPA_API_URL = 'https://api.chapa.dev'
CHAPA_WEBHOOK_URL = 'http://127.0.0.1:8000/'
CHAPA_API_VERSION = 'v1'
CHAPA_TRANSACTION_MODEL = 'chapa_payment.ChapaTransaction'

EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = EMAIL_PORT
DEFAULT_FROM_EMAIL = DEFAULT_FROM_EMAIL
