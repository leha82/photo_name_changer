# json file and files management module

import json
import datetime

def getConfig(filename):
    with open('config.json') as json_file:
        json_data = json.load(json_file)

        dir = json_data["directory"]
        format = json_data["name_format"]

    return dir, format

def getFilenamebyFormat(dateTime, filenameFormat):
    dt = datetime.datetime.strptime(dateTime, '%Y:%m:%d %H:%M:%S')

    filename = filenameFormat
    filename = filename.replace('[year]', f'{str(dt.year):0>4}')
    filename = filename.replace('[month]', f'{str(dt.month):0>2}')
    filename = filename.replace('[day]', f'{str(dt.day):0>2}')
    filename = filename.replace('[hour]', f'{str(dt.hour):0>2}')
    filename = filename.replace('[minute]', f'{str(dt.minute):0>2}')
    filename = filename.replace('[second]', f'{str(dt.second):0>2}')
    return filename

# dir, format = getConfig('config.json')
# print(dir)
# print(format)

# fn = getFilenamebyFormat("2020:08:31 18:09:28", format, 1)
# print(fn)