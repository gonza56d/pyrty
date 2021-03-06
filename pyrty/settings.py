import os

from celery.schedules import crontab


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '1cca#y=o2xcrx(kd_9!fpq&ykaej_m36q^d%*0tdjiex9l2uoc'

DEBUG = True

ALLOWED_HOSTS = []

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_quill',
]

PROJECT_APPS = [
    'comments.apps.CommentsConfig',
    'forums.apps.ForumsConfig',
    'notifications.apps.NotificationsConfig',
    'posts.apps.PostsConfig',
    'privatemessages.apps.PrivateMessagesConfig',
    'profiles.apps.ProfilesConfig',
    'subforums.apps.SubforumsConfig',
    'summaryreports.apps.SummaryreportsConfig',
    'users.apps.UsersConfig',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ]
}

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'utils.middlewares.LoginFormMiddleware',
    'utils.middlewares.NotificationMiddleware',
    'utils.middlewares.PrivateMessageMiddleware',
]

# Django Quill
QUILL_CONFIGS = {
    'default':{
        'theme': 'snow',
        'modules': {
            'syntax': True,
            'toolbar': [
                [
                    {'font': []},
                    {'header': []},
                    {'align': []},
                    'bold', 'italic', 'underline', 'strike', 'blockquote',
                    {'color': []},
                    {'background': []},
                ],
                ['code-block', 'link'],
                ['clean'],
            ]
        }
    }
}

ROOT_URLCONF = 'pyrty.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'pyrty.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': 5432,
    }
}

# DATABASES['default']['ATOMIC_REQUESTS'] = True

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

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

STATIC_URL = '/static/'

LOGIN_URL = 'signup'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Auth user override
AUTH_USER_MODEL = 'users.User'

# Auth backend override
AUTHENTICATION_BACKENDS = ['users.backends.UserBackend']

# Celery conf
CELERY_BROKER_URL = 'amqp://rabbitmq:5672'
CELERY_RESULT_BACKEND = 'amqp://rabbitmq:5672'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Argentina/Buenos_Aires'
