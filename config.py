import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-a-secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:123456jj@localhost/enrollment'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = os.environ.get('STATIC_FOLDER') or 'static'
    TEMPLATE_FOLDER = os.environ.get('TEMPLATE_FOLDER') or 'templates'