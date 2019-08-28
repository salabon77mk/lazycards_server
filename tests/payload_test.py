#!/usr/bin/python3

import requests

payload = {"word":"toaster", "deck":"Default", "apiact":"word", "ankact":"addNote"}
print(requests.post("http://127.0.0.1:5000", json = payload))
#print(requests.post("http://192.168.1.226/", json = payload))
