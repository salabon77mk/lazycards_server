#!/usr/bin/python3
"""Contains functions responsible for CRUD ops on NOTES"""
import anki_connect_key_values as ac
import android_json_keys as jk

import payload_generator
import server_comm


def add_note(app_data, api_response):
    """
    :param app_data: JSON body from the LazyCards Android app
    :param api_response: The response acquired for that word
    :return:
    """
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
    """
    :param api_response:
    :return: A formatted version of the api_response that looks like this:
    -----------------------------

    KEY_1: Word_1
    Word_2

    KEY_2: Word_3
    Word_4

    ---------------------------
    """
    b = "<br>"
    string_rep = ""
    for i in api_response:
        for (k, v) in i.items():
            string_rep += b + "<b>" + k + "</b>" + ": "
            if type(v) is list:
                for s in v:
                    string_rep += s + b
            else:
                string_rep += v + b
        string_rep += b + "<hr>"
    return string_rep
