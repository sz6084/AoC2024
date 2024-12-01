## PART ONE ##
import pathlib

lines = pathlib.Path("input.txt").read_text().split("\n")
colOne = []
colTwo = []

for value in lines:
    value = value.split()
    colOne.append(int(value[0]))
    colTwo.append(int(value[-1]))
colOne.sort()
colTwo.sort()
#print(colOne)
#print(colTwo)
dist = 0
for i in range(0,len(lines)):
    dist+=abs(colOne[i]-colTwo[i])
print(dist)

## PART TWO ##

similarity = 0

for val1 in colOne:
    occurences = colTwo.count(val1)
    similarity+=val1*occurences
print(similarity)