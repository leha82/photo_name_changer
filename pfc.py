# Photo Filename Changer
# 사진 파일이름 변환기
# 사진과 파일 이름의 메타데이터를 읽어와 사진을 찍은 시간 순으로 정렬합니다.
# 사진 json 포맷에 있는 내용대로  파일 이름을 수정하는 프로그램입니다.

import os
import FileModule as fmodule
import PhotoModule as pmodule

jsonFile = "config.json"

# get configuration directory and format from json file
pathDir, fileFormat = fmodule.getConfig(jsonFile)

# open file path and find all files int the path
# pathDir = "C:\\Users\\Owner\\Desktop\\photo\\test_file"
files = os.listdir(pathDir)

# print(type(files))

# check the files and make fileList when it is a file, not directory

fileList = []

for fileName in files:
    pathName = os.path.join(pathDir,fileName)
    if os.path.isfile(pathName):
        fileList.append(pathName)

# rename the files to "1.jpg, 2.jpg ..."

newFileList = []

index = 1
for fullName in fileList:
    filePath = os.path.dirname(fullName)
    fileName = os.path.basename(fullName)
    fileExt = os.path.splitext(fileName)

    dateTime = pmodule.getLatestDateTime(fullName)

    modifiedName = fmodule.getFilenamebyFormat(dateTime, fileFormat)
    newFilename = modifiedName + fileExt[1].lower()
    newFullName = os.path.join(filePath,newFilename)

    tempFileName = str(index) + fileExt[1].lower()
    tempFullName = os.path.join(filePath,tempFileName)

    os.rename(fullName, tempFullName)
    newFileList.append([newFullName, tempFullName])

    print(index, ":", fullName, "->", tempFullName)
    index+=1

newFileList.sort()

lastName = ""
count = 0

for i in range(0, len(newFileList)):
    newName = newFileList[i][0]
    tempName = newFileList[i][1]
    filePath = os.path.dirname(newName)
    fileName = os.path.basename(newName)
    fileExt = os.path.splitext(fileName)

    if fileName == lastName:
        count += 1
    else:
        count = 0
        if (i+1) < len(newFileList):
            nextName = os.path.basename(newFileList[i+1][0])
            if fileName == nextName:
                count = 1
    
    if count!=0:
        newFileName = fileExt[0] + '_' + f'{str(count):0>2}' + fileExt[1].lower()
        newName = os.path.join(filePath, newFileName)
    
    print(i, "[", fileName , "]:", tempName, "->", newName)
    os.rename(tempName, newName)

    lastName = fileName
