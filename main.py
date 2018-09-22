#! /usr/bin/env python
# coding: utf-8

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello main blue application"

@app.route("/sub")
def hello_world():
    return "Hello sub blue application"
