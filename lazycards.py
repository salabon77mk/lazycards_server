#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import requests

import json

from http import HTTPStatus

from flask import Flask
from flask import request
from flask import jsonify

import anki_req
import api_handler
import words_api
import server_comm
import decks_endpoint_handler

app = Flask(__name__)


# Jsonify the response, might not be needed
def handle_anki_response(res):
    # craft a flask response
    if res == HTTPStatus.INTERNAL_SERVER_ERROR:
        return ""
    else:
        return jsonify(res)


# Create a custom Flask response that tells the server is down
# Might not be needed must test with app first
def server_unavailable_res():
    return ""

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


# Get the available decks on Anki
# This data will populate the drop down menu in LazyCards
@app.route("/get_decks", methods=['GET'])
def decks_get():
    if not server_comm.is_running():
        return HTTPStatus.SERVICE_UNAVAILABLE

    res = decks_endpoint_handler.get_deck_names()
    return res


if __name__ == "__main__":
    app.run()

