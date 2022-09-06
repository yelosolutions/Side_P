#!/usr/bin/python3
import json

"""manipulate json file"""
with open("friends.json") as f:
    data = json.load(f)
    
for friend in data["friends"]:
    del friend["name"]
    print(friend)

with open('new.json', 'w') as f: 
    json.dump(data, f, indent=2)

