"""Config object to configure database and env variables."""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Config object contains database and env variables."""

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://localhost:5432/rfid_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False