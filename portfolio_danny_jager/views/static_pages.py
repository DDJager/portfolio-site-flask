from flask import Blueprint, render_template, current_app as app

static_pages = Blueprint('static_pages', __name__, template_folder='templates')

@static_pages.route('/')
def home():
    """ The homepage of the website """
    return render_template('base.html')

@static_pages.route('/about')
def about():
    """ The about page of the website """
    return 'Welcome to my about page'
