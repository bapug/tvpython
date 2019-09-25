print("Running development settings")

from .common import *

DEBUG = True

ENABLE_DEBUG_TOOLBAR = DEBUG and env.str('ENABLE_DEBUG_TOOLBAR', default=False)

if ENABLE_DEBUG_TOOLBAR:
    MIDDLEWARE += [
        'djdev_panel.middleware.DebugMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

if DEBUG:
    INSTALLED_APPS += [
        'django_extensions',
        'django_nose',
    ]

if ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS += ['debug_toolbar', ]

STATICFILES_DIRS += [DJANGO_ROOT('static'),]


DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'LOCATION': 'bapug_flake'
    }
}



