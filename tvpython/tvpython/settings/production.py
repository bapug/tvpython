print("Running production settings")

from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "django",
        "USER": "django",
        "PASSWORD": "Wouldn't you like to know!!"
    }
}

RAVEN_CONFIG = {
    'dsn': 'https://f1fac260d9cd4ae58ffc9e99b9753394:a38e8f83965b45789d621cb3425a2833@app.getsentry.com/48492',
}

INSTALLED_APPS = INSTALLED_APPS + (
    # Add Raven for production
    'raven.contrib.django.raven_compat',
)