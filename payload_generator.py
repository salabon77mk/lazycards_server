#!/usr/bin/python3
"""Creates the payloads for AnkiConnect"""

_ACTION = "action"
_VERSION_STR = "version"
_VERSION_INT = 6
_PARAMS = "params"


def gen_payload_no_params(action):
    """
    Generates the payload for the AnkiConnect queries that only have two keys
    :param action: The action AnkiConnect will perform
    :return:
    """
    payload = {
        _ACTION: action,
        _VERSION_STR: _VERSION_INT
    }
    return payload


def gen_payload_with_params(action, params):
    """
    Generates the payload for the AnkiConnect queries that include the 'params' key
    :param action: The action AnkiConnect will perform
    :param params: The value for _PARAMS. This part is crafted in one of the endpoint files
    :return:
    """
    payload = {
        _ACTION: action,
        _VERSION_STR: _VERSION_INT,
        _PARAMS: params
    }
    return payload
