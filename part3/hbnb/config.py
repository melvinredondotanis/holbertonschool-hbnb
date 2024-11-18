import os
from datetime import timedelta
from dotenv import load_dotenv


class DefaultAdmin:
    DEFAULT_HBNB_ADMIN_ID = '36c9050e-ddd3-4c3b-9731-9f487208bbc1'
    DEFAULT_HBNB_ADMIN_FIRST_NAME = 'Admin'
    DEFAULT_HBNB_ADMIN_LAST_NAME = 'HBnB'
    DEFAULT_HBNB_ADMIN_PASSWORD = 'admin1234'
    DEFAULT_HBNB_ADMIN_EMAIL = 'admin@hbnb.io'


class Config:
    load_dotenv()
    DEBUG = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY',
                               'xXx_im_the_best_developer_xXx')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_ALGORITHM = 'HS512'
    JWT_DECODE_ALGORITHMS = ['HS512']


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'admin': DefaultAdmin
}
