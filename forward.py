#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import cgitb
import requests
import cgi
#cgitb.enable()    
#COMMENT TEST

import anki_req
import api_handler
print("Content-Type: text/html; charset=utf-8")
print()
print()

#qs = cgi.FieldStorage()
qs = {"word":"toaster", "deck":"Default", "apiact":"word", "ankact":"addNote"}
data = api_handler.res(qs)

#check if data is good, otherwise maybe a false word or action was used

success = anki_req.handle(data, qs)

print(success)
