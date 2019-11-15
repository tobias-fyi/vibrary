"""
vibrary :: Definition of the vibrary database models.
"""

from flask_sqlalchemy import SQLAlchemy

# Import the database
DB = SQLAlchemy()


class Word(DB.Model):
    """Individual words."""

    id = DB.Column(DB.Integer, primary_key=True)
    word = DB.Column(DB.String(32), nullable=False)
    definition = DB.Column(DB.String(480), nullable=True)

    def __repr__(self):
        return f"<Word {self.word}>"


class Phrase(DB.Model):
    """A table of phrases, which are made up of Words."""

    id = DB.Column(DB.Integer, primary_key=True)
    body = DB.Column(DB.Unicode(240))

    def __repr__(self):
        return f"<Phrase '{self.body}'>"
