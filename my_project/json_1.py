#!/usr/bin/python3

import json

friends_string = '''
{
    "friends": [
        {
            "name": "Rono Kamau",
            "age": "23",
            "email" :"ronokamau@gmail.com",
            "has_grilfriend": false
        },
        {
            "name": "Wangai Guru",
            "age": "24",
            "email" :"wangaiguru@gmail.com",
            "has_grilfriend": true
        }
    ]
}
'''

data = json.loads(friends_string)
for friend in data["friends"]:
    print(friend["name"])
