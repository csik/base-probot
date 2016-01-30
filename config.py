import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    SECRET_KEY = 'this-really-needs-to-be-changed'
    TESTING = False
    CSRF_ENABLED = True
    SECURITY_PASSWORD_SALT = 'salt-licker'

    #  SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_POOL_RECYCLE = 280
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #  mail settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    CONTACT_EMAIL = os.environ['CONTACT_EMAIL']

    #  gmail authentication
    MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']

    #  mail accounts
    MAIL_DEFAULT_SENDER = 'flask_starter.promo@gmail.com'

    #  flask user
    USER_ENABLE_CONFIRM_EMAIL = True

    #  remote logging
    LOGGING_URL = os.environ['LOGGING_URL']


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    ROOT_URL = 'http://127.0.0.1:5000'


class ProductionConfig(Config):
    DEBUG = False
    ROOT_URL = None


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = False
    ROOT_URL = ''