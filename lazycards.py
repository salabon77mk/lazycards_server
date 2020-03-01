#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import requests

import json

from http import HTTPStatus

from flask import Flask
from flask import request
from flask import jsonify

import notes_endpoint_handler
import words_api
import server_comm
import decks_endpoint_handler
import android_json_keys
import errors

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world"


# Will handle CRUD ops relating to cards
@app.route("/add_note", methods=['POST'])
def add_note():
    if not server_comm.is_running():
        return errors.ANKI_DOWN

    data = request.get_json()
    api = data[android_json_keys.API]

    new_word_json = None
    if api == android_json_keys.Apis.WORDS:
        new_word_json = words_api.new_word(data[android_json_keys.WORD], data[words_api.OPTIONS])
    elif api == android_json_keys.Apis.NONE:
        return notes_endpoint_handler.add_note(data, "")

    # In case we got an http error response from above
    if errors.is_error(new_word_json):
        return new_word_json

    return notes_endpoint_handler.add_note(data, new_word_json)


# Get the available decks on Anki
# This data will populate the drop down menu in LazyCards
@app.route("/get_decks", methods=['GET'])
def decks_get():
    if not server_comm.is_running():
        return errors.ANKI_DOWN

    return decks_endpoint_handler.get_deck_names()


@app.route("/test_new_card_words", methods=['GET'])
def test_create():
    qs = {
        "word": "ergerg",
        "deck": "MORE",
        "tags": [""],
        "options": ["definition", "synonyms"]}
    new_word_json = words_api.new_word(qs["word"], qs["options"])
    if errors.is_error(new_word_json):
        return new_word_json

    return notes_endpoint_handler.add_note(qs, new_word_json)


@app.route("/test_new_card_none", methods=['GET'])
def test_create_with_no_api():
    qs = {
        "word": "HELLO",
        "back": "WORLD",
        "deck": "TEST",
        "tags": [""]
    }

    return notes_endpoint_handler.add_note(qs, "")

if __name__ == "__main__":
    app.run()

