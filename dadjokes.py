#dadjokes.py

import requests
import json

url ="https://icanhazdadjoke.com/"
header = {"Accept":"application/json"}
print("Want to hear a joke?\n")
userschoice = input("Enter a search term for a dad joke by topic or hit Enter for a random joke? ")
if userschoice == "":
    resp = requests.get(url, headers=header)
    data = resp.json()['joke']
    print(data)
else:
    uri = url + "search?term=" + userschoice
    resp = requests.get(uri, headers=header)
    data = resp.json()
    totaljokes = data['total_jokes']
    if totaljokes > 10: totaljokes = 10
    for n in range(0,totaljokes):
        print(data['results'][n]['joke'])    


