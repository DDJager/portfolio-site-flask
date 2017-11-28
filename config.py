""" The configuration file. """

class Config(object):
    HELLO = 'world!'

class DevelopmentConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/development'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/production'

# Create a dictionary of the Config classes
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
