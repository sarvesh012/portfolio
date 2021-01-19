from .base import *

# SECURITY CHECK run:  python manage.py check --deploy

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

INTERNAL_IPS = [ '127.0.0.1', ]

ALLOWED_HOSTS = ['10.24.102.196', 'localhost', 'demo.net']

SITE_ID = 1
#MEDIA_ROOT = "/home/ubuntu/media"
STATIC_ROOT = '/home/ubuntu/static'

# SECURE_BROWSER_XSS_FILTER = True # xss protection - old browsers

# CSRF_COOKIE_SECURE = True #CSRF cookies only via HTTPS
# SESSION_COOKIE_SECURE = True #Session cookies only via HTTPS

# SECURE_HSTS_SECONDS = 3153600 # =1year HTTPS only
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True # Subdomains HTTPS only
# SECURE_HSTS_PRELOAD = True # tell browser to preload HTTPS

# SECURE_SSL_REDIRECT = True # redirect HTTP requests to HTTPS


# AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
# AWS_S3_REGION_NAME = os.environ['AWS_S3_REGION_NAME']
# AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
# AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
# AWS_S3_CUSTOM_DOMAIN = os.environ['AWS_S3_CUSTOM_DOMAIN']


