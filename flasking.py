__author__ = 'Liew'

from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
import database
import json
import collections
import webbrowser

app = Flask(__name__)

@app.route("/")
def hello():
    c = database.getimage()
    e = json.loads(c[0])
    d = collections.OrderedDict(sorted(e.items()))
    di = [dict(a=row[0], b=row[1]) for row in d.items()]
    print di
    return render_template('hello.html', hello=di)



def starting():
    app.run()

starting()