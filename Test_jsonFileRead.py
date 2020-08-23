# json File Read test code

import json

with open('config.json') as json_file:
    json_data = json.load(json_file)

    dir = json_data["directory"]
    format = json_data["name_format"]