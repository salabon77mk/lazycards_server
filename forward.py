#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import cgitb
import requests
import cgi
#cgitb.enable()    
#COMMENT TEST

import api_handler
print("Content-Type: text/html; charset=utf-8")
print()
print()

#data = api_handler.res(cgi.FieldStorage())
data = api_handler.res({"word":"toast", "deck":"ing", "action":"word"})

#check if data is good, otherwise maybe a false word or action was used
#print("HELLOOOOOO")
#print(data)

r = requests.post('http://127.0.0.1:8765', json = {
    "action": "addNote",
    "version": 6,
    "params": {
        "note": {
            "deckName": "Default",
            "modelName": "Basic",
            "fields": {
                "Front": "front content",
                "Back": "back content"
            },
            "options": {
                "allowDuplicate": False
            },
            "tags": [
                "yomichan"
            ]
        }
    }
})

print(r.json())
