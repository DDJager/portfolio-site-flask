from flask import Blueprint, render_template, current_app as app

portfolio = Blueprint('portfolio', __name__, template_folder='templates')

@portfolio.route('/portfolio')
def index():
    """ Return all portfolio items """
    return 'Welcome to my portfolio page'
