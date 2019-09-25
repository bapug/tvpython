print("Running development settings")

from .common import *

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'LOCATION': 'tennisblock_flake'
    }
}

FIXTURE_DIRS = (
    PROJECT_ROOT('fixtures'),
)


