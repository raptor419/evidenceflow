# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from app.home.models import getSummary, getWords
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound



@blueprint.route('/index')
def index():
    return render_template('index.html', segment='index')

@blueprint.route('/summary_result',methods=['POST','GET'])
def summary():
    if request.method == 'POST':
        content = request.form['keyword']
        y = getSummary(content)
        content = [content]
        if y == None:
            y = ["Word not found"]
        return render_template('summary_result.html',result  = [content,y])
    else:
        return render_template('summary.html')


@blueprint.route('/algebra_result',methods=['POST','GET'])
def algebra():
    if request.method == 'POST':
        positive = request.form['positive']
        negative = request.form['negative']
        positive = positive.split(",")
        negative = negative.split(",")
        for i in range(len(positive)):
            positive[i] = positive[i].lower()
            positive[i] = ''.join(positive[i].split())
        for i in range(len(negative)):
            negative[i] = negative[i].lower()
            negative[i] = ''.join(negative[i].split())
        if positive[0] == "":
            positive = []
        if negative[0] == "":
            negative = []
        words = getWords(positive,negative)
        equation = ""
        for w in positive:
            equation = equation + " + " + w
        for w in negative:
            equation = equation + " - " + w
        return render_template('algebra_result.html',result  = [words,equation])
    else:
        return render_template('algebra.html')

@blueprint.route('/<template>')
def route_template(template):

    try:

        if not template.endswith( '.html' ):
            template += '.html'

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( template, segment=segment )

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500

# Helper - Extract current page name from request 
def get_segment(request): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
