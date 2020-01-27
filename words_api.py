#!/usr/bin/python3
"""Handles requests that use the Words API"""
import requests
import copy
from flask import Flask
from http import HTTPStatus

import errors

# Most important keys in the Words API Response
RESULTS = "results"

# These are the options for what to include in the final new word body
# The options can be found in the response body from words namely in RESPONSE[_RESULTS] (a list)
# IF THESE ARE EDITED MAKE SURE TO EDIT Words_API.java in the app
OPTIONS = "options" # part of the JSON post request from the app
_EVERYTHING = "EVERYTHING"
_DEFINITION = "definition"
_SYNONYMS = "synonyms"
_ANTONYMS = "antonyms"
_EXAMPLES = "examples"

# Error codes that words API can respond with
_BAD_REQUEST = 400
_UNAUTHORIZED = 401
_WORD_NOT_FOUND = 404
_INTERNAL_SERVER_ERROR = 500
_ERRORS = {_BAD_REQUEST, _UNAUTHORIZED, _WORD_NOT_FOUND, _INTERNAL_SERVER_ERROR}


app = Flask(__name__)

api_key = ""
with app.open_resource('apikey.txt') as f:
    api_key = f.read().rstrip()

def_url = "https://wordsapiv1.p.rapidapi.com"

headers = {
    'x-rapidapi-host':  "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': api_key
}


# Option list is never empty
def new_word(word, option_list):
    """
    Gets response from the Words API
    :param word: What word will be part of the API
    :param option_list: User specified options. This data originates in the Android app
    :return: Results list from the API response
    """
    action = "/words/"
    url = def_url + action + word
    response = requests.get(url, headers=headers)

    if response.status_code != HTTPStatus.OK:
        return errors.http_error(response.status_code)

    data = response.json()
    option_set = set()
    for op in option_list:
        option_set.add(op)

    if _EVERYTHING in option_set:
        return data[RESULTS]

    return craft_finished_card(data, option_set)


def craft_finished_card(words_api_response, option_set):
    """
    Clean the response body of options that user did not specify
    We return the results of the body, we don't need the word, pronunciation, syllables, at least I think?

    :param words_api_response: JSON api response
    :param option_set: User specified set of options to include in the final card (Definition, Synonyms, etc..
    :return: Returns the RESULTS segment of the api response, don't need the rest of the body
    """
    response_copy = copy.deepcopy(words_api_response)
    res = response_copy[RESULTS]

    for i in range(len(res)):
        for (k, v) in res[i].items():
            if k not in option_set:
                del words_api_response[RESULTS][i][k]

    return words_api_response[RESULTS]

