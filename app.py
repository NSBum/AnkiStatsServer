from flask import Flask
from flask import request, jsonify, session
from flask.ext.sqlalchemy import SQLAlchemy
import os
import json

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from models import *

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/data', methods=['POST'])
def handle_save_stats():
    #   get JSON data
    data = request.get_json(silent=True)

    stat = Stats(data)

    db.session.add(stat)
    db.session.commit()

    return jsonify(result={"status": 200},id = stat.s_id)


if __name__ == '__main__':
    app.run()
