import os 
from os import environ
from pickle import FALSE


class Config(object):

    DEBUG = False
    TESTING = False

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = "Jak3Sn8ke123!"

    UPLOADS = "/home/username/app/app/static/uploads"

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(object):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class DebugConfig(object):
    DEBUG = False

