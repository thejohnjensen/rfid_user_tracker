"""Config object to configure database and env variables."""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Config object contains database and env variables."""

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'top_secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
