#!/usr/bin/env python3
"""
A basic Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """A configuration class for a flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> str:
    """Display a simple html page"""
    return render_template('1-index.html')
