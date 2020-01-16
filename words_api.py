#!/usr/bin/python3
import requests
import copy
from flask import Flask
from http import HTTPStatus

import errors

# Most important keys in the Words API Response
RESULTS = "results"
WORD = "word"

# These are the options for what to include in the final new word body
# The options can be found in the response body from words namely in RESPONSE[_RESULTS] (a list)
# IF THESE ARE EDITED MAKE SURE TO EDIT Words_API.java in the app
_EVERYTHING = "everything"
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
    response_copy = copy.deepcopy(words_api_response)
    res = response_copy[RESULTS]

    for i in range(len(res)):
        for (k, v) in res[i].items():
            if k not in option_set:
                del words_api_response[RESULTS][i][k]

    return words_api_response

