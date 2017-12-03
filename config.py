""" The configuration file. """

class Config(object):
    SITE_NAME = 'Danny Portfolio'

class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    SECRET_KEY = '<secret_key_here>'
    DATABASE_URI = 'mysql://user@localhost/development'

class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'mysql://user@localhost/production'

# Create a dictionary of the Config classes
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
