## PART ONE ##
import pathlib, re

lines = pathlib.Path("input.txt").read_text().split("\n")

total = 0

def checkHorizontal(lines):
    total_inner = 0
    for line in lines:
        matches = re.findall(r'(?=(XMAS))', line)
        matches += re.findall(r'(?=(SAMX))', line)
        total_inner+=len(matches)
    return total_inner
def checkVertical(lines):
    total_inner = 0
    lines_transposed = list(map(''.join, zip(*lines)))
    total_inner+=checkHorizontal(lines_transposed)
    return total_inner

#horizontal
total+=checkHorizontal(lines)

#vertical
total+=checkVertical(lines)

#diag1
lines_copy = lines[:]
for i in range(len(lines_copy)):
    lines_copy[i] = i*"."+lines_copy[i]+"."*(len(lines_copy[i]) - i)
total+=checkVertical(lines_copy)

#diag2
lines_copy = lines[:]
for i in range(len(lines_copy)):
    lines_copy[i] = "."*(len(lines_copy) - i)+lines_copy[i]+i*"."
total+=checkVertical(lines_copy)
print(total)

## PART TWO ##

new_total = 0

def checkMAS(lines, i, j):
    total_inner = 0
    if "MAS" == (lines[i-1][j-1]+lines[i][j]+lines[i+1][j+1]):
        total_inner+=1
    if "SAM" == (lines[i-1][j-1]+lines[i][j]+lines[i+1][j+1]):
        total_inner+=1
    if "MAS" == (lines[i-1][j+1]+lines[i][j]+lines[i+1][j-1]):
        total_inner+=1
    if "SAM" == (lines[i-1][j+1]+lines[i][j]+lines[i+1][j-1]):
        total_inner+=1
    return total_inner
for i in range(1, len(lines)-1):
    for j in range(1, len(lines[i])-1):
        if "A" == lines[i][j]:
            if checkMAS(lines, i, j)>=2:
                new_total+=1

print(new_total)