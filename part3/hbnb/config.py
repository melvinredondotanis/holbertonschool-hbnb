import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'xXx_im_the_best_developer_xXx')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
