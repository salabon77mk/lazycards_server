#!/usr/bin/python3

import words_api

# Currently only connects to one api, but can be expanded upon further
# Change up args to accept a dict
def res(args):
    if len(args) < 3:
        print("Too few arguments")
        exit()

    word = args["word"]
    deck = args["deck"]
    action = args["action"]
    switcher={
            "word": words_api.new_word(word)
    }
    return switcher.get(action)
