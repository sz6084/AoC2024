## PART ONE ##
import pathlib, re

line = pathlib.Path("input.txt").read_text()

disk_map = []
file = 1
fileCounter = 0
for i in range(len(line)):
    if file==1:
        for i in range(int(line[i])):
            disk_map.append(fileCounter)
        file*=-1
        fileCounter+=1
    elif file==-1:
        for i in range(int(line[i])):
            disk_map.append(None)
        file*=-1

while None in disk_map:
    disk_map[disk_map.index(None)] = disk_map[-1]
    del disk_map[-1]

#for item in disk_map:
#    if item==None:
#        print(".", end='')
#    else:
#        print(item, end='')

checksum = 0
for i in range(len(disk_map)):
    checksum+=i*disk_map[i]
print(checksum)