# modules for photo metadata
import os
import time
from PIL import Image, ExifTags

def getLatestDateTime(file_path):
    img = Image.open(file_path)
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }

    # print(exif)
    # for item in exif.items():
    #     if item[0] != 'MakerNote':
    #         print(item[0], item[1])

    atime = time.localtime(os.path.getatime(file_path))
    mtime = time.ctime(os.path.getmtime(file_path))
    ctime = time.ctime(os.path.getctime(file_path))

    print()

    datetimes = []
    datetimes.append(exif.get("DateTime"))
    datetimes.append(exif.get("DateTimeOriginal"))
    datetimes.append(exif.get("DateTimeDigitized"))
    datetimes.append(time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(os.path.getatime(file_path))))
    datetimes.append(time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(os.path.getmtime(file_path))))
    datetimes.append(time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(os.path.getctime(file_path))))

    # print("DateTime", ":", exif.get("DateTime"))
    # print("DateTimeOriginal", ":", exif.get("DateTimeOriginal"))
    # print("DateTimeDigitized", ":", exif.get("DateTimeDigitized"))

    # print("Access time", ":", time.ctime(os.path.getatime(file_path)))
    # print("Modified time", ":", time.ctime(os.path.getmtime(file_path)))
    # print("Change time", ":", time.ctime(os.path.getctime(file_path)))

    new_dt = []
    for dt in datetimes:
        # print(dt)
        if dt != None:
            new_dt.append(dt)

    new_dt.sort()

    # print()

    # for dt in new_dt:
    #     print(dt)
    return new_dt[0]

file_path = "1_photo.jpg"
datetime = getLatestDateTime(file_path)
print("datetime :", datetime)