#!/usr/bin/python3

import words_api

# Currently only connects to one api, but can be expanded upon further
def res(args = []):
    if len(arguments) < 3:
        print("Too few arguments")
        exit

    word = args[0]
    deck = args[1]
    action = args[2]

    switcher={
            "word": newWord(word)
    }
    return switcher.get(action)
