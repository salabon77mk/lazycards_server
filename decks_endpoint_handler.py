#!/usr/bin/python3
"""
Crafts the payloads for AnkiConnect actions that involve the Decks
"""
import requests
import payload_generator
import server_comm


def get_deck_names():
    """Retrieves the deck names in Anki, NOT their IDs"""
    payload = payload_generator.gen_payload_no_params("deckNames")
    return server_comm.send_and_receive_payload(payload)

