"""
:: Vibrary :: 

A simple Flask application for analyzing and predicting tweets.
"""

from flask import Flask, render_template
from dotenv import load_dotenv

from vibrary.models import DB, Word, Phrase


load_dotenv()


def create_app():
    """
    App factory.
    
    Returns
    -------
    app
        Flask app.
    """

    # Define the application
    app = Flask(__name__)

    # Configure the database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize DB-app connection
    DB.init_app(app)

    @app.route("/")
    def home():
        """
        Home page route.
        
        Returns
        -------
        html/jinja2 template
            Returns 'home.html', inheriting from 'base.html'.
        """

        # Set the words variable using query object
        words = User.query.all()

        return render_template("home.html", title="Home", words=users)

    return app
