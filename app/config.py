class Config:
  '''
  General configuration parent class
  '''
  NEWS_API_BASE_URL1 ="https://newsapi.org/v2/everything?q={}&apiKey={}"
  NEWS_API_BASE_URL2="https://newsapi.org/v2/everything?language=en&apiKey={}"
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True