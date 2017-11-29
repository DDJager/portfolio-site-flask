from flask import Blueprint

models = Blueprint('models', __name__)

@models.route('/models')
def index():
    return 'models'
