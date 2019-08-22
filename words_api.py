#!/usr/bin/python3
import requests
from os import path

f = open("apikey.txt", "r")
api_key = f.read().rstrip()

def_url = "https://wordsapiv1.p.rapidapi.com"

headers = {
    'x-rapidapi-host':  "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': api_key
}

def new_word(word):
    action = "/words/"
    url = def_url + action + word
#    print(url)
    return res(url)
    


def res(url):
    res = requests.get(url, headers=headers)
    # if res is not a 404 return it
#    print(res)
#    print(res.json())
    return res.json()
