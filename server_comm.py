#!/usr/bin/python3

import requests
import payload_generator

import json

from http import HTTPStatus

HOST = 'http://127.0.0.1:8765'


# Check to see if connection is alive
def is_running():
    payload = payload_generator.gen_payload_no_params("version")
    try:
        requests.post(HOST, json=payload)
        return True
    except:
        return False


def send_and_receive_payload(payload):
    res = requests.post(HOST, json=payload)
    if res.status_code == 200:
        return json.loads(res.content)
    return HTTPStatus.INTERNAL_SERVER_ERROR


