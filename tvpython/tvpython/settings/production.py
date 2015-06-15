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

