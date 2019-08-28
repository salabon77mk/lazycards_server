#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import requests
import json

from flask import Flask
from flask import request

import anki_req
import api_handler

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def default():
    qs = {"word":"toaster", "deck":"Default", "apiact":"word", "ankact":"addNote"}
    dat = request.get_json()
    data = api_handler.res(qs)
    print(qs)
    success = anki_req.handle(data, qs)
    return qs

if __name__ == "__main__":
    app.run()

"""
#check if data is good, otherwise maybe a false word or action was used


print(success)
"""
