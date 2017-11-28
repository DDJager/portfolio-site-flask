"""
This file starts the project and development server.
"""

# Import the create_app() method from the main package's __init__.py file
from portfolio_danny_jager import create_app

# Instantiate the Flask object with the given configurations
app = create_app('development')

# Run the app
app.run()
