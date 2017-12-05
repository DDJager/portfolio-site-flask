# Import main files
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import config

# Import Blueprints
from portfolio_danny_jager.models import models
from portfolio_danny_jager.views import portfolio, static_pages, admin_panel

def create_app(config_name = 'production'):
    """
    Factory pattern: Instantiate a Flask object from this method.

    :return: Flask instance
    """

    # Create new instance of a flask object
    app = Flask(__name__)
    Bootstrap(app)

    # If in development mode, auto reload the jinja templates
    if config_name == 'development':
        app.jinja_env.auto_reload = True

    # Set the Configuration object from config.py
    app.config.from_object(config.app_config[config_name])

    # Register the blueprints
    app.register_blueprint(models)
    app.register_blueprint(portfolio.portfolio, url_prefix='/portfolio')
    app.register_blueprint(static_pages.static_pages)
    app.register_blueprint(admin_panel.admin_panel, url_prefix='/notsosecretadminpanel')


    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    # Return the flask object
    return app
