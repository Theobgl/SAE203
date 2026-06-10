"""
Django settings for Drive Alimentaire project.
"""

import os
import sys
from pathlib import Path
from mongoengine import connect

# Force UTF-8 encoding sur Windows
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-test-key-change-in-production'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'app',
]

# Ajouter les apps Django seulement pour SQLite
MONGODB_ENABLED = False

try:
    # Teste RÉELLEMENT la connexion MongoDB
    from mongoengine import connect, ValidationError
    import socket

    # First, test if MongoDB is actually running on localhost:27017
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # 2 secondes timeout
        result = sock.connect_ex(('127.0.0.1', 27017))
        sock.close()

        if result != 0:
            raise ConnectionError("MongoDB port not accessible")
    except:
        raise ConnectionError("MongoDB is not running")

    # Si accessible, établir la connexion
    connect(
        db='drive_alimentaire',
        host='localhost',
        port=27017,
        connect=True,  # Vraie connexion
        serverSelectionTimeoutMS=2000
    )
    MONGODB_ENABLED = True
    DATABASES = {
        'default': {
            'ENGINE': 'mongoengine',
            'NAME': 'drive_alimentaire',
        }
    }
    print("[OK] MongoDB connected successfully!")

except Exception as e:
    # Fallback à SQLite pour développement
    print(f"[INFO] MongoDB unavailable")
    print("[INFO] Using SQLite for development...")
    MONGODB_ENABLED = False

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    print("[OK] SQLite enabled as fallback!")

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'fr-FR'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
