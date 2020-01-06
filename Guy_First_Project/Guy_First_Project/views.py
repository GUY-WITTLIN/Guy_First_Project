"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Guy_First_Project import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Hi, My Name Is Guy Wittlin'
    )

@app.route('/album')
def album():
    """Renders the about page."""
    return render_template(
        'PictureAlbum.html',
        title='This Is My Picture Album',
        year=datetime.now().year,
        message='The Biggest Wins Of The Best National & Club Teams In Football (From 2010-2019):'
    )