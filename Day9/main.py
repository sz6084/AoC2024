## PART ONE ##
import pathlib

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
print(checksum) # run time 38 secs

## PART TWO ##

# find blank runs, find non-contiguous blocks
# move non-contiguous blocks that fit into blank runs
# treat blocks as files

# i%2 = 0
for i in range(len(disk_map)-1, 0):
    if i % 2 != 0:
        if disk_map[i]