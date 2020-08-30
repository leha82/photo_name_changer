# modules for photo metadata
import os
import time
from PIL import Image, ExifTags

def getLatestDateTime(file_path):
    img = Image.open(file_path)
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }

    datetimes = []
    datetimes.append(exif.get("DateTime"))
    datetimes.append(exif.get("DateTimeOriginal"))
    datetimes.append(exif.get("DateTimeDigitized"))
    datetimes.append(time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(os.path.getatime(file_path))))
    datetimes.append(time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(os.path.getmtime(file_path))))
    datetimes.append(time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(os.path.getctime(file_path))))

    # print("Image info - DateTime", ":", datetimes[0])
    # print("Image info - DateTimeOriginal", ":", datetimes[1])
    # print("Image info - DateTimeDigitized", ":", datetimes[2])
    # print("File info - Access time", ":", datetimes[3])
    # print("File info - Modified time", ":", datetimes[4])
    # print("File info - Change time", ":", datetimes[5])

    new_dt = []
    for dt in datetimes:
        if dt != None:
            new_dt.append(dt)

    new_dt.sort()

    return new_dt[0]

# file_path = "2_photo.jpg"
# datetime = getLatestDateTime(file_path)
# print("datetime :", datetime)