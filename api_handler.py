#!/usr/bin/python3

import errors
import words_api

# Currently only connects to one api, but can be expanded upon further
# Change up args to accept a dict
def res(args):
    errors.check_arg(args)

    word = args["word"]
    api_act = args["apiact"]
#    api_choice = args["apichoice"]
    switcher={
            "word": words_api.new_word(word)
    }
    return switcher.get(apiact)
