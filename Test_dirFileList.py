# Test for getting file list from given directory
# Test for rename files

import os

# open file path and find all files int the path
path_dir = "C:\\Users\\Owner\\Desktop\\photo\\test_file"
files = os.listdir(path_dir)

# print(type(files))

# check the files and make file_list when it is a file, not directory

file_list = []

for file_name in files:
    path_name = os.path.join(path_dir,file_name)
    if os.path.isfile(path_name):
        file_list.append(path_name)

# rename the files to "1.jpg, 2.jpg ..."

index = 0
for file_fullname in file_list:
    index += 1
    file_path = os.path.dirname(file_fullname)
    file_name = os.path.basename(file_fullname)
    file_ext = os.path.splitext(file_name)
    new_name = os.path.join(file_path,str(index)+file_ext[1].lower())

    # os.rename(file_fullname, new_name)

    print(index, ":", file_fullname, "|", file_ext, "->", new_name)
    

    

