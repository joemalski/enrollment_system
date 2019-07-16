import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    STATIC_FOLDER = os.environ.get('STATIC_FOLDER') or 'static'
    TEMPLATE_FOLDER = os.environ.get('TEMPLATE_FOLDER') or 'templates'