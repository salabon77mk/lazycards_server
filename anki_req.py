#!/usr/bin/python3
import errors
import requests
import json

VERSION = 6
HOST = 'http://127.0.0.1:8765'

payload_np = {
    "action": None,
    "version": VERSION
}


# def otherwise
payload_temp = {
    "action": None,
    "version": VERSION,
    "params" : {}
}


# Check to see if connection is alive
def is_running():
    payload_np["action"] = "version"
    try:
        requests.post(HOST, json=payload_np)
        return True
    except:
        return False


def deck_exists(deck):
    payload_np["action"] = "deckNames"
    res = requests.post(HOST, json=payload_np).json()
    decks = res["result"]

    if deck in decks:
        return True
    return False


def handle(data, args):
    errors.check_arg(args)

    word = args["word"]
    deck = args["deck"]
    ankact = args["ankact"]

    if is_running() is False:
        print("No connection to Anki")
        exit()

    switcher={
        "addNote": add_note(data, word, deck)
    }
    return switcher.get(ankact)


# later implement tags
def add_note(data, word, deck):
    if deck_exists(deck) is False:
        print("Deck does not exist")
        return False
    

    defs = ""
    results = data["results"]

    for i in results:
        defs += i["definition"] + "<br><br>"

    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": deck,
                "modelName": "Basic",
                "fields": {
                    "Front": word,
                    "Back": defs
                },
                "options": {
                    "allowDuplicate": False
                },
                "tags": [
                    "IMPLEMENT LATER"
                ]
            }
        }
    }
    return requests.post(HOST, json=payload)