#!/usr/bin/env python
import json
import requests

google_link = 'http://suggestqueries.google.com/complete/search?output=firefox&hl=en&q='

def get_suggestions(query):
    query = query.replace(' ', '+')
    response = requests.get(google_link + query)
    return response

def pprint(s):
    print(json.dumps(s, indent=4))

phrases = ['what time', 'where is', 'is spiderman']

raw_results = [ get_suggestions(t) for t in phrases ]

res = [ { x[0] : x[1] } for x in [ z.json() for z in raw_results ] ]

pprint(results)
