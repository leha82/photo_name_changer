# Test for setting filename by the format

import datetime

filename_format = "[year][month][day]_[hour][minute][second]_[sequence]"
test_dt = "2020:08:01 18:09:28"

now = datetime.datetime.now()
print(now)

nowDate = now.strftime('%Y:%m:%d')
print(nowDate)

dt = datetime.datetime.strptime(test_dt, '%Y:%m:%d %H:%M:%S')
print(dt)

dt2 = datetime.datetime.strftime(dt, '%Y%m%d_%H%M%S_')
print(dt2 + str(1))


test_index = 1
new_filename = filename_format
print("file format : ", new_filename)
new_filename = new_filename.replace('[year]', f'{str(dt.year):0>4}')
new_filename = new_filename.replace('[month]', f'{str(dt.month):0>2}')
new_filename = new_filename.replace('[day]', f'{str(dt.day):0>2}')
new_filename = new_filename.replace('[hour]', f'{str(dt.hour):0>2}')
new_filename = new_filename.replace('[minute]', f'{str(dt.minute):0>2}')
new_filename = new_filename.replace('[second]', f'{str(dt.second):0>2}')
# new_filename = new_filename.replace('[sequence]', f'{str(test_index):0>2}')

print("new file name : ", new_filename)


