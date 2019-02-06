from flask import render_template,request,redirect,url_for
from app import app
import urllib.request
import json
from .request import get_sources

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    source = get_sources('sources')
    return render_template('index.html',source = source)
