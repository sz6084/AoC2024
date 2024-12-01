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
    dist+=abs(int(colOne[i])-int(colTwo[i]))
print(dist)