#!/usr/bin/python
# encoding: utf-8
import flask
import platform
import datetime

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return "Hello from: " + platform.node() + ", timestamp: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3003)
