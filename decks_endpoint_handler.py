#!/usr/bin/python3

import requests
import payload_generator
import server_comm


def get_deck_names():
    payload = payload_generator.gen_payload_no_params("deckNames")
    return server_comm.send_and_receive_payload(payload)

