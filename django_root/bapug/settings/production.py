print("Running production settings")

from .common import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "django",
        "USER": "django",
        "HOST": 'localhost',
        "PASSWORD": "Wouldn't you like to know!!"
    }
}

