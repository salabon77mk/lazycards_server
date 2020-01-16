#!/usr/bin/python3

import requests
import json

import payload_generator
import errors

HOST = 'http://127.0.0.1:8765'


# Check to see if connection is alive
# The reasoning behind the payload structure of this can be found in "how to check connection" in AnkiConnect
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

    return errors.AnkiConnectError


