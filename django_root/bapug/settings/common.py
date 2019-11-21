from email.utils import parseaddr
import environ
import os
from os.path import join, exists
from email.utils import getaddresses
import sys
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
CONF_DIR = environ.Path(__file__)
DJANGO_ROOT = CONF_DIR - 3
PROJECT_ROOT = DJANGO_ROOT - 1
BASE_DIR = DJANGO_ROOT - 1

print(f"DJANGO_ROOT:{DJANGO_ROOT}")
print(f"PROJECT_ROOT:{PROJECT_ROOT}")

sys.path.append(PROJECT_ROOT("scripts"))

# DEBUG
DEBUG = env.bool("DJANGO_DEBUG", False)

# DATABASE
DATABASES = {
    'default': {
        **{
            'ATOMIC_REQUESTS': True,
            'CONN_MAX_AGE': 10,
        },
        **env.db("DATABASE_URL", default='postgresql://django:@localhost/bapug'),
    }
}

print("Databases: {}".format(DATABASES['default']))

# Security Options
SECRET_KEY = env.str('SECRET_KEY')
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', default=True)
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', default=True)
X_FRAME_OPTIONS = 'DENY'
SECURE_BROWSER_XSS_FILTER = True

SESAME_MAX_AGE = 30

WAGTAIL_SITE_NAME = env.str("WAGTAIL_SITE_NAME", default="bapug.org")

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[WAGTAIL_SITE_NAME])

# This allows us to specify admins in an environment file as a list.
default_admins = ['Ed Henderson <ed@bapug.org>']
ADMINS = [parseaddr(addr) for addr in env.list("ADMINS", default=default_admins)]
MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "America/Denver"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = env.int("SITE_ID", default=1)


# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = PROJECT_ROOT("site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = PROJECT_ROOT("site_media", "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/site_media/static/"

# Additional locations of static files
STATICFILES_DIRS = [
    PROJECT_ROOT("static"),
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = "d*aa!bub3ecc^nsix50ripam1!g!o^1l78(k65ogk2cdds_gcq"

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [DJANGO_ROOT("templates"),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ]
        }
    }
]

# Disable CSRF to make it easier to use REST client
# Only do this temporarily, might make some API calls work when they shouldn't
if DEBUG and env.bool('DISABLE_CSRF', default=False):
    MIDDLEWARE.remove('django.middleware.csrf.CsrfViewMiddleware')

ROOT_URLCONF = "bapug.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "bapug.wsgi.application"
ASGI_APPLICATION = 'bapug.routing.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '200/hour',
        'user': '1000/hour',
    }
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",

    # Wagtail
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.routable_page',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.contrib.table_block',
    'wagtail.contrib.settings',
    'modelcluster',
    'taggit',

    # theme
    #"bootstrapform",
    #"pinax_theme_bootstrap",

    # external
    "account",

    # project
    "bapug",
    "frontend",
]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'root': {
        'level': 'WARNING',
        'handlers': ['mail_admins'],
    },
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s',
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': '/tmp/gardentronic_debug.log',
        },
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': True,
        },
        'django': {
            'handlers': ['console', 'file'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django_test': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console', 'mail_admins'],
            'propagate': False,
        },
        'django.utils.autoreload': {
            'level': 'ERROR',
        }

    },
}


FIXTURE_DIRS = [
    PROJECT_ROOT("fixtures"),
]

CACHES = {
    'default': {
        **env.cache('REDIS_URL', default='dummycache://')
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [env.str("CHANNELS_REDIS_URI", default="")],
        },
    },
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ACCOUNT_OPEN_SIGNUP = False
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
ACCOUNT_LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2

AUTHENTICATION_BACKENDS = [
    "account.auth_backends.UsernameAuthenticationBackend",
]

