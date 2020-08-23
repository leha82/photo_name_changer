# This Create "config.json" file which is json for configuration of this project

import json
from collections import OrderedDict

file_data = OrderedDict()

file_data["directory"] = "C:\\Users\\Owner\\Desktop\\photo"
file_data["name_format"] = "[year][month][day]_[hour][minute][second]_[sequence]"

print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

with open('config.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
    
