import pathlib

lines = pathlib.Path("input.txt").read_text().split("\n")
colOne = []
colTwo = []

for value in lines:
    colOne.append(value[0])
    colTwo.append(value[-1])
colOne.sort()
colTwo.sort()
print(colOne)
print(colTwo)
dist = 0
for i in range(0,len(lines)):
    if colOne[i]>colTwo[i]:
        dist+=int(colOne[i])-int(colTwo[i])
    else:
        dist+=int(colTwo[i])-int(colOne[i])
print(dist)