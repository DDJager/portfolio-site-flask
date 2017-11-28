from flask import Flask
import config

def create_app(config_name = 'production'):
    """
    Factory pattern: Instantiate a Flask object from this method.

    :return: Flask instance
    """

    # Create new instance of a flask object
    app = Flask(__name__)

    # Set the Configuration object from config.py
    app.config.from_object(config.app_config[config_name])

    @app.route('/')
    def index():
        return app.config['DATABASE_URI']

    # Return the flask object
    return app
