from flask import Blueprint, render_template, current_app as app

admin_panel = Blueprint('admin_panel', __name__, template_folder='templates')

@admin_panel.route('/')
def index():
    """ Return all portfolio items """
    return render_template('admin-panel.html')
