""" The configuration file. """

class Config(object):
    SITE_NAME = 'Danny Portfolio'
    HELLO = 'world!'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'mysql://user@localhost/development'

class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'mysql://user@localhost/production'

# Create a dictionary of the Config classes
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
