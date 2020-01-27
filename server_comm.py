#!/usr/bin/python3
"""
This is the link between the Flask App and the AnkiConnect API
Provide methods for:
1. Checking if Anki is up
2. Submitting payload body to AnkiConnect and sending back the response
"""


import requests
import json
from http import HTTPStatus

import payload_generator
import errors

_HOST = 'http://127.0.0.1:8765'


def is_running():
    """
    Check to see if connection is alive
    The reasoning behind the payload structure of this can be found in "how to check connection" in AnkiConnect
    """
    payload = payload_generator.gen_payload_no_params("version")
    try:
        requests.post(_HOST, json=payload)
        return True
    except:
        return False


def send_and_receive_payload(payload):
    """
    Sends the payload crafted in one of the endpoint files
    :param payload:
    :return: Sends back the AnkiConnect response unless there was an error
    """
    res = requests.post(_HOST, json=payload)
    if res.status_code == HTTPStatus.OK:
        return json.loads(res.content)

    return errors.AnkiConnectError


