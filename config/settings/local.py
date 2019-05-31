from .base import *

SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='l7k9_q7v4rnb4ki$ih$l9tu=g(^6q183tncwgm_)!cs3+(uo#i'
)

DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '192.168.88.105',
    '192.168.88.*',
    '192.168.88.106',
    '192.168.88.107',
    '192.168.88.102',
    '192.168.88.103',
    '192.168.88.1',
    '192.168.88.2',
    '192.168.88.3',
    '192.168.88.4',
    '192.168.88.5',
    '172.17.140.73',
    '0.0.0.0',
    '*'
]

# REST_FRAMEWORK['HIDE_DOCS'] = True
