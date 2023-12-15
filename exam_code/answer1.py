
lines=open('/dshome/WoongLab/heo/midterm_homework/ta_20231027201612.csv',encoding='cp949').read().splitlines()[7:]
del lines[-2:]
import csv

with open('/dshome/WoongLab/heo/midterm_homework/temperature-daejeon.csv',mode='w',encoding='utf-8') as csvfile:
    writer=csv.writer(csvfile)
    for row in csv.reader(lines):
        row[0]=row[0].lstrip()
        writer.writerow(row)
    else:
        print('The file is saved!')