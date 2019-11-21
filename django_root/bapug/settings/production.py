print("Running production settings")

from .common import *

STATIC_ROOT = BASE_DIR('collectedstatic')

# Security settings for production
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

loggers = LOGGING['loggers']
loggers['django_test']['handlers'] = []
loggers['django.db.backends']['handlers'] = ['mail_admins']
