import os

class Config:
  '''
  general configuration class
  '''
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?language=en&apiKey={}'
  NEWS_API_KEY = 'b58639b93a564639907c634b2cd74203'
  NEWS_API_BASE_URL2 = 'https://newsapi.org/v2/everything?sources=bbc-news,al-jazeera-english,cnn,independent,google-news,the-telegraph,mashable,the-lad-bible,buzzfeed,bloomberg,engadget,espn,fortune&sortBy=publishedAt&pageSize=100&apiKey={}'


class ProdConfig(Config):
    '''
    production config class
    '''
    pass


class DevConfig(Config):
    '''
    dev config class
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
