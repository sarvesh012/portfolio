from .base import *

# SECURITY CHECK run:  python manage.py check --deploy

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['allkoci.com', '127.0.0.1']

# SECURE_BROWSER_XSS_FILTER = True # xss protection - old browsers

# CSRF_COOKIE_SECURE = True #CSRF cookies only via HTTPS
# SESSION_COOKIE_SECURE = True #Session cookies only via HTTPS

# SECURE_HSTS_SECONDS = 3153600 # =1year HTTPS only
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True # Subdomains HTTPS only
# SECURE_HSTS_PRELOAD = True # tell browser to preload HTTPS

# SECURE_SSL_REDIRECT = True # redirect HTTP requests to HTTPS