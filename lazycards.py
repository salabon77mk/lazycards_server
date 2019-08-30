#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import requests
import json

from flask import Flask
from flask import request

import anki_req
import api_handler

app = Flask(__name__)

@app.route("/api_resolve", methods=['GET', 'POST'])
def default():
    qs = {"word":"toaster", "deck":"Default", "apiact":"word", "ankact":"addNote"}
    dat = request.get_json()
    data = api_handler.res(qs)
#    success = anki_req.handle(data, qs)
    return data

if __name__ == "__main__":
    app.run()

@app.route("/anki_sub", methods=['POST'])
def anki_sub(data):
    return ""


# Will accept an array of JSON that will hold api requests
@app.route("/file_post", methods=['POST'])
def file_post(data):
    return  ""

"""
#check if data is good, otherwise maybe a false word or action was used


print(success)
"""
