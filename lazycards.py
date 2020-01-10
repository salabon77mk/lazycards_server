#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import requests

import json

from flask import Flask
from flask import request

import anki_req
import api_handler
import words_api

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"


@app.route("/api_resolve", methods=['POST', 'GET'])
def default():
    qs = {"word":"toaster", "deck":"Default", "apiact":"word", "ankact":"addNote"}
    req = request.get_json()
    data = api_handler.res(qs)
#    success = anki_req.handle(data, qs)
    return data


@app.route("/anki_sub", methods=['POST'])
def anki_sub(data):
    return ""


# Will accept an array of JSON that will hold api requests
@app.route("/file_post", methods=['POST'])
def file_post(data):
    return  ""


# Simplest route, least customization, just add a definition and be done
@app.route("/fast_sub", methods=['POST'])
def fast_sub():
    data = request.get_json()
    res = words_api.new_word(data["word"])
    success = anki_req.fast_handle(res, data)
    return ""


if __name__ == "__main__":
    app.run()
    #    app.run(host = '0.0.0.0')
