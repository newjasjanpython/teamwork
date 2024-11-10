

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

APPEND_SLASH=False

CORS_ALLOW_ALL_ORIGINS = False  # Disable allowing all origins
CORS_ALLOWED_ORIGINS = [
    'https://yourfrontenddomain.com',  # Add the actual domain of your frontend app
    'http://localhost:3000',  # Example for local dev environment
]





SECRET_KEY = 'django-insecure-2fc$wg*k2v)#$hd+cblzle1oac@io6a@w+!oclzh-!$8w7ps41'


DEBUG = True
ALLOWED_HOSTS = ["*"]



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    'quiz',
    'user',
    'api'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",

]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    
]


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'




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


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # Adjust based on your needs
    ],
}



# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Additional locations the staticfiles app will traverse if the FileSystemFinder finder is enabled.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]



# Absolute filesystem path to the directory that will hold user-uploaded files.
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

AUTH_USER_MODEL = 'user.CustomUser'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

