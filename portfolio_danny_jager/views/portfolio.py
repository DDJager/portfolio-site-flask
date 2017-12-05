from flask import Blueprint, render_template, current_app as app

portfolio = Blueprint('portfolio', __name__, template_folder='templates')

@portfolio.route('/')
def index():
    """ Return all portfolio items """
    return render_template('portfolio.html')

@portfolio.route('/<int:portfolio_id>')
def item(portfolio_id):
    """ Return all portfolio items """
    return render_template('portfolio-item.html')
