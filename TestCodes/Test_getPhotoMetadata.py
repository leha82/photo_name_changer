# test for getting metadata of photo file
import os
import time
from PIL import Image, ExifTags

file_path = "1_photo.jpg"
img = Image.open(file_path)
exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }

print(exif)
for item in exif.items():
    print(item)

datetimes = []
datetimes.append(exif.get("DateTime"))
datetimes.append(exif.get("DateTimeOriginal"))
datetimes.append(exif.get("DateTimeDigitized"))
datetimes.append(time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(os.path.getatime(file_path))))
datetimes.append(time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(os.path.getmtime(file_path))))
datetimes.append(time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(os.path.getctime(file_path))))

print("DateTime", ":", datetimes[0])
print("DateTimeOriginal", ":", datetimes[1])
print("DateTimeDigitized", ":", datetimes[2])
print("Access time", ":", datetimes[3])
print("Modified time", ":", datetimes[4])
print("Change time", ":", datetimes[5])

new_dt = []
for dt in datetimes:
    if dt != None:
        new_dt.append(dt)

new_dt.sort()

print()

for dt in new_dt:
    print(dt)

print("datetime :", new_dt[0])

if datetimes[1] == None:
    print("DateTime Original is none")
