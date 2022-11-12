import requests

#GET request query for '/' endpoint 
query = requests.get('http://127.0.0.1:7777/')

print(query.text)