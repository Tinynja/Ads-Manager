import os


class DevConfig:
    DEBUG = True
    SECRET_KEY = 'e34ba621-e0c9-423b-8931-2d94202f471b'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/ads_manager.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True


class ProdConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')  # Postgres
