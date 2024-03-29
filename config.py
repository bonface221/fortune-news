import os

class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    # NEWS_API_KEY='9098cc99aef349a79fc8e7e3f899c70b'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY =os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options={
    'development' : DevConfig,
    'production' : ProdConfig
}
