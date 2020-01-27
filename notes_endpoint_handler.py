#!/usr/bin/python3
"""Contains functions response for CRUD ops on NOTES"""

import requests
import anki_connect_key_values as ac
import android_json_keys as jk

import payload_generator
import server_comm


import json

# Anki Actions


# later implement tags
def add_note(app_data, api_response):
    """
    :param app_data: JSON body from the LazyCards Android app
    :param api_response: The response acquired for that word
    :return:
    """
    print(api_response)
    _ADD_NOTE = "addNote"
    params = {
        ac.NOTE: {
            ac.DECKNAME: app_data[jk.DECK],
            ac.MODEL_NAME: ac.BASIC,
            ac.FIELDS: {
                ac.FRONT: app_data[jk.WORD],
                ac.BACK: __add_note_parse_words(api_response)
            },
            ac.OPTIONS: {
                ac.ALLOW_DUPLICATE: False
            },
            ac.TAGS: list(app_data[jk.TAGS])
        }
    }
    payload = payload_generator.\
        gen_payload_with_params(_ADD_NOTE, params)

    return server_comm.send_and_receive_payload(payload)


def __add_note_parse_words(api_response):
    b = "<br>"
    skip = "<br><br>"
    double_skip = "<br><br><br>"
    string_rep = ""
    for i in api_response:
        for (k, v) in i.items():
            string_rep += k + ": "
            if type(v) is list:
                for s in v:
                    string_rep += s + b
            else:
                string_rep += v + skip
        string_rep += double_skip + "<hr>"
    print(string_rep)
    return string_rep







