print("Running development settings")

from .common import *

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'LOCATION': 'bapug_flake'
    }
}

FIXTURE_DIRS = (
    PROJECT_ROOT('fixtures'),
)


