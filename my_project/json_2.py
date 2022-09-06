#!/usr/bin/python3

import json

friends_string = '''
{
    "friends": [
        {
            "name": "Rono Kamau",
            "age": "23",
            "email": "ronokamau2gmail.com",
            "has_girlfriend": false
        },
        {
            "name": "Wangai Guru",
            "age": "24",
            "email": "wangaiguru@gmail.com",
            "has_girlfriend": true
        }
    ]
}
'''
data = json.loads(friends_string)

for friend in data['friends']:
    del friend["name"]

new_string = json.dumps(data, indent=
        ;i2)
print(new_string)
