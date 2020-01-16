#!/usr/bin/python3

ACTION = "action"
VERSION_STR = "version"
VERSION_INT = 6
PARAMS = "params"


def gen_payload_no_params(action):
    # No parameters
    payload = {
        ACTION: action,
        VERSION_STR: VERSION_INT
    }
    return payload


# Could put the params as an argument?
def gen_payload_with_params(action, params):
    payload = {
        ACTION: action,
        VERSION_STR: VERSION_INT,
        PARAMS: params
    }
    return payload
