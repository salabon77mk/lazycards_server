#!/usr/bin/python3

VERSION = 6


def gen_payload_no_params(action):
    # No parameters
    payload = {
        "action": action,
        "version": VERSION
    }
    return payload


# Could put the params as an argument?
def gen_payload_with_params():
    payload = {
        "action": None,
        "version": VERSION,
        "params": {}
    }
    return payload