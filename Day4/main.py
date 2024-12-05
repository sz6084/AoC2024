## PART ONE ##
import pathlib, re

lines = pathlib.Path("exinput.txt").read_text().split("\n")

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
    try:
        if "MAS" == (lines[i-1][j-1]+lines[i][j]+lines[i+1][j+1]):
            total_inner+=1
            print("MAS \\",total_inner)
        if "SAM" == (lines[i-1][j-1]+lines[i][j]+lines[i+1][j+1]):
            total_inner+=1
            print("SAM \\",total_inner)
        if "MAS" == (lines[i+1][j-1]+lines[i][j]+lines[i-1][j+1]):
            total_inner+=1
            print("MAS /",total_inner)
        if "SAM" == (lines[i+1][j-1]+lines[i][j]+lines[i-1][j+1]):
            total_inner+=1
            print("SAM /",total_inner)
        print("ret:",total_inner)
        return total_inner
    except:
        print("fail")
        return total_inner
1
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if "A" == lines[i][j]:
            if checkMAS(lines, i, j)>=2:
                new_total+=1

print(new_total)