import os
from datetime import timedelta


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'xXx_im_the_best_developer_xXx')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
