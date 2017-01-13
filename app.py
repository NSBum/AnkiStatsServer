from flask import Flask, Response
from flask import request, jsonify, session
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

import os
import json
import pygal
from pygal.style import DarkSolarizedStyle
from datetime import date, datetime, timedelta

USE_PRODUCTION_SERVER = 0

app = Flask(__name__)
app.config.from_object('config')

#   see if this keeps db connection alive
app.config['SQLALCHEMY_POOL_SIZE'] = 100
app.config['SQLALCHEMY_POOL_RECYCLE'] = 7200

db = SQLAlchemy(app)

from models import *

def diff_month(d1, d2):
	return (d1.year - d2.year)*12 + d1.month - d2.month

def tsminmax(timestamps):
    tsmin = datetime.fromtimestamp(min(timestamps))
    tsmax = datetime.fromtimestamp(max(timestamps))
    return (tsmin,tsmax)

def datelabels(timestamps):
    (tsmin, tsmax) = tsminmax(timestamps)
    datestart = date(tsmin.year, tsmin.month, 01)
    monthdelta = diff_month(tsmax, tsmin)
    steps = min(monthdelta/4,1)
    [datestart + timedelta(x*365/12) for x in range(0,monthdelta+1) ]

@app.route('/')
def index():
    title = 'Test chart'

    return render_template('index.html', title=title)

@app.route('/vocabnotes/')
def vocabnotes():
    title = 'Russian vocabulary notes'
    return render_template('vocabnotes.html', title=title)

@app.route('/newtime/')
def newtime():
    title = 'New cards/time'
    return render_template('newtime.html', title=title)

@app.route('/graph/')
def graph():
    statlist = Stats.query.order_by(Stats.timestamp.asc()).all()
    stamps = [s.timestamp for s in statlist]
    vocabs = [s.vocab for s in statlist]

    dateline = pygal.DateLine(x_label_rotations=25)
    dateline.x_labels = datelabels(stamps)

    dateline.add("Vocab notes",zip(stamps,vocabs))
    return Response(response=dateline.render(), content_type='image/svg+xml')

@app.route('/grnewtime/')
def newTimeGraph():
    statlist = Stats.query.order_by(Stats.timestamp.asc()).all()
    stamps = [s.timestamp for s in statlist]
    durs = [s.duration for s in statlist]
    totals = [s.tcount for s in statlist]

    #   compute the increase in card number
    totals1 = totals[1:]
    news = [0] + [x2-x1 for (x1,x2) in zip(totals,totals1)]

    graph = pygal.DateLine(x_label_rotations=25,secondary_range=(0,30))
    graph.x_labels = datelabels(stamps)
    graph.add("New cards",zip(stamps,news),secondary=True)
    graph.add("Duration (s)",zip(stamps,durs))
    return Response(response=graph.render(), content_type='image/svg+xml')

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/vocab')
def handle_vocab_req():
    stat = Stats.query.order_by(Stats.timestamp.desc()).first()
    return jsonify(result={"status":200},vocab=stat.vocab)

@app.route('/data', methods=['POST'])
def handle_save_stats():
    #   get JSON data
    data = request.get_json(silent=True)

    stat = Stats(data)

    db.session.add(stat)
    db.session.commit()

    return jsonify(result={"status": 200},id = stat.s_id)

if __name__ == '__main__':
    if USE_PRODUCTION_SERVER == 1:
        from tornado.wsgi import WSGIContainer
        from tornado.httpserver import HTTPServer
        from tornado.ioloop import IOLoop
        import tornado.options

        print 'starting app on tornado server, port 5000'
        http_server = HTTPServer(WSGIContainer(app))
        http_server.listen(5000)
        IOLoop.instance().start()

        app.debug = False
    else:
        print 'starting on port 5000'
        app.run('0.0.0.0', port=5000, debug=True)
