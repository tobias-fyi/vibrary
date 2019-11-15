"""
vibrary.__init__ :: Entry point for vibrary Flask app.
"""

from .app import create_app

# APP is global variable
APP = create_app()
