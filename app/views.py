import datetime
from flask import render_template, request, redirect
from app import app, db, parse

@app.route('/', methods=['GET'])
def home():
    text = parse.parseFile('/Users/zucker/Codebase/personal/tps/app/static/text/kundera.txt')
    return render_template('base.html', title="tps", heading=text)