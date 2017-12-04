""" The configuration file. """

class Config(object):
    SITE_NAME = 'Danny Portfolio'
    SITE_TITLE = 'Welcome to the portfolio website of Danny Jager!'

class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    SEND_FILE_MAX_AGE_DEFAULT = 0
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
