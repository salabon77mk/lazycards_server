#!/usr/bin/python3
import requests
from flask import Flask

app = Flask(__name__)
api_key = ""
with app.open_resource('apikey.txt') as f:
    api_key = f.read().rstrip()

def_url = "https://wordsapiv1.p.rapidapi.com"

headers = {
    'x-rapidapi-host':  "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': api_key
}


def new_word(word):
    action = "/words/"
    url = def_url + action + word
    return res(url)


def res(url):
    res = requests.get(url, headers=headers)
    # if res is not a 404 return it
    return res.json()
