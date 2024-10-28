
import os
from pathlib import Path
from datetime import timedelta
# import storages


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o0t@y-r*w2@+7vuoei@n1v4gf+9fdno(2i8qhkixay__$e336n'

UNSPLASH_ACCESS_KEY = 'LyxWs8x3_x67M0TY1rJIBRs62SZmctEjXY7BBgzJtjY'

# API KEY OF CHATGPT
#OPENAI_API_KEY = os.getenv('sk-proj-sk-B4iqIYMcRPs19hDexi5fPnwoushKynIOyzps2FOPw4T3BlbkFJaI_rgmzOAiJEd9ub6QETxBqx_p9paDyyN8HNhOylMA')

# TravelPowers API
TRAVELPOWERS_API_URL = 'https://api.travelpayouts.com/v2/hotels'
TRAVELPOWERS_API_TOKEN = '0a6f7834ea89890fa426297697129e5f'

# facebook
FACEBOOK_APP_ID = '1433449907291745'
FACEBOOK_APP_SECRET = '9e3213a9c9c572c2918269981fa192f3'
FACEBOOK_REDIRECT_URI = 'https://localhost:8000/sync/facebook/callback/'  # URL for the callback

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.becompany.net'
EMAIL_PORT = 993  # Or 465 for SSL
EMAIL_USE_TLS = True  # Or EMAIL_USE_SSL = True for SSL
EMAIL_HOST_USER = 'connect@becompany.net'
EMAIL_HOST_PASSWORD = 'FfyZM=9rV.d]'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = [
    "https://becart.net",
    "http://becart.net",
    "https://bebackend.net",
    "http://bebackend.net"
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django_otp',
    'django_otp.plugins.otp_totp',

    # Third party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'channels',
    'storages',

    # Local apps

    # 'asset',
    'user',
    # 'customer',
    # 'cloudditor',
    'business',
    # 'employee',
    # 'project',
    'location',
    # 'ecommerce',
    # 'bookkeeping',
    # 'promotion',
    'telecom',
    'sync',
    'settings',
    # 'chat',
]

commit = 'commit'
# Auth
AUTH_USER_MODEL = 'user.User'

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django_otp.middleware.OTPMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

# Jwt

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=50),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# Root URL
ROOT_URLCONF = 'backend.urls'

# Template
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

# WSGI
WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bedb',
        'USER': 'mysuperuser',
        'PASSWORD': 'A053730730a',
        'HOST': 'bedb.cr2ywaqoihsx.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

SITE_ROOT = BASE_DIR


MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
MEDIA_URL = '/media/'


STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AWS - KEYS
AWS_ACCESS_KEY_ID = 'AKIA3FRRISIPEE54YA7O'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'be-company-storage'
AWS_S3_SIGNATURE_NAME = 's3v4'
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERIFY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
