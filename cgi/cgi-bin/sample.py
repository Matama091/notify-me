#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html")
print()   

form = cgi.FieldStorage()

for key in form:
    value = form[key].value
    print('<p>%s: %s</p>' % (key, value))

# $ python3 -m http.server --cgi 8000