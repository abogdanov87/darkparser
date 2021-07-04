from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    '37.140.192.51',
    'darkparser.ru',
    'www.darkparser.ru',
]

MIDDLEWARE += [
    'django.middleware.csrf.CsrfViewMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u1344503_default',
        'USER': 'u1344503_default',
        'PASSWORD': 'N_7Q2iDd',
        'HOST': 'localhost',
    }
}

BASE_URL = 'https://www.darkparser.ru'
LOGIN_FORM_URL = BASE_URL + '/admin/json/api-auth/login/'
HOME_FORM_URL = BASE_URL + '/#/'

LOGOUT_REDIRECT_URL = LOGIN_FORM_URL
LOGIN_REDIRECT_URL = LOGIN_FORM_URL
LOGIN_URL = LOGIN_FORM_URL

STATIC_ROOT = os.path.join(BASE_DIR, RELATIVE_PATH, '../static/')