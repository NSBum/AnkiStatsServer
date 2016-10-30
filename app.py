from flask import Flask
from flask import request, jsonify, session
from flask.ext.sqlalchemy import SQLAlchemy

import os
import json

USE_PRODUCTION_SERVER = 1

app = Flask(__name__)
app.config.from_object('config')

#   see if this keeps db connection alive
app.config['SQLALCHEMY_POOL_SIZE'] = 100
app.config['SQLALCHEMY_POOL_RECYCLE'] = 7200

db = SQLAlchemy(app)

from models import *

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/vocab')
def handle_vocab_req():
    stat = Stats.query.last()
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
