#!/usr/bin/python3

ANKI_DOWN = ("", 503)
ANKI_CONNECT_ERROR = ("", 500)


def http_error(http_resp):
    return "", http_resp


def is_error(data):
    if type(data) is tuple:
        return True
    return False


