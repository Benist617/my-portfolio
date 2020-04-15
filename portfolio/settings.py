import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '_7q3@g+o48s&sc+pvm@65x4pd7oe3#+tfh(z^qpqf-pc#!(%6@'
DEBUG = True

ALLOWED_HOSTS = ['portfolio-project-ist.herokuapp.com', '127.0.0.1']

INSTALLED_APPS = [
    'projects.apps.ProjectsConfig',
    'todoapp.apps.TodoappConfig',
    'pollapp.apps.PollappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

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

WSGI_APPLICATION = 'portfolio.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'portfoliodb',
#         'USER': 'postgres',
#         'PASSWORD': '123456',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

DATABASES = {'default': dj_database_url.config(default='postgres://postgres:123456@localhost/portfoliodb')}



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
TIME_ZONE = 'Asia/Jerusalem'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
# C:\Users\benis\Desktop\my_portfolio\myenv\static
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]

#live
# C:\Users\benis\Desktop\my_portfolio\myenv\static
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


#live
# C:\Users\benis\Desktop\my_portfolio\myenv\media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


MEDIA_URL = '/media/'
