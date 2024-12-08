## PART ONE ##
import pathlib, re

lines = pathlib.Path("exinput.txt").read_text().split("\n")
guardLocation = [-1,-1]
guardDir = "^"
symbols = ["^",">","v","<"]
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] in symbols:
            guard_location = [i, j]
            guard_dir = lines[i][j]

lines_copy = lines[:]
def checkMoveRotate(guardDir):
    # rotate symbols so less if statements? like a lazy susan?
    if (guardDir=="^" and lines[guardLocation[0]-1][guardLocation[1]]=="#"):
        lines[guardLocation[0]] = lines[guardLocation[0]][:guardLocation[1]] + ">" + lines[guardLocation[0]][guardLocation[1]+1:]
        guardDir = ">"
    else:
        lines[guardLocation[0]] = lines[guardLocation[0]][:guardLocation[1]] + "X" + lines[guardLocation[0]][guardLocation[1]+1:]
        if guardLocation[0]!=0:
            guardLocation[0]-=1
        lines[guardLocation[0]] = lines[guardLocation[0]][:guardLocation[1]] + "^" + lines[guardLocation[0]][guardLocation[1]+1:]
    if (guardDir==">" and lines[guardLocation[0]][guardLocation[1]+1]=="#"):
        lines[guardLocation[0]] = lines[guardLocation[0]][:guardLocation[1]] + "v" + lines[guardLocation[0]][guardLocation[1]+1:]
        guardDir = "v"
    else:
        lines[guardLocation[0]] = lines[guardLocation[0]][:guardLocation[1]] + "X" + lines[guardLocation[0]][guardLocation[1]+1:]
        if guardLocation[1]!=len(lines[0])-1:
            guardLocation[1]+=1
        lines[guardLocation[0]] = lines[guardLocation[0]][:guardLocation[1]] + "v" + lines[guardLocation[0]][guardLocation[1]+1:]
    if (guardDir=="v" and lines[guardLocation[0]+1][guardLocation[1]]=="#"):
        lines[guardLocation[0]] = lines[guardLocation[0]][:guardLocation[1]] + "<" + lines[guardLocation[0]][guardLocation[1]+1:]
        guardDir = "<"
    else:
        lines[guardLocation[0]] = lines[guardLocation[0]] = lines[guardLocation[0]][:guardLocation[1]] + "X" + lines[guardLocation[0]][guardLocation[1]+1:]
        if guardLocation[0]!=len(lines)-1:
            guardLocation[0]+=1
        lines[guardLocation[0]] = lines[guardLocation[0]][:guardLocation[1]] + "v" + lines[guardLocation[0]][guardLocation[1]+1:]
    if (guardDir=="<" and lines[guardLocation[0]][guardLocation[1]-1]=="#"):
        lines[guardLocation[0]] = lines[guardLocation[0]][:guardLocation[1]] + "^" + lines[guardLocation[0]][guardLocation[1]+1:]
        guardDir = "^"
    else:
        lines[guardLocation[0]] = lines[guardLocation[0]][:guardLocation[1]] + "X" + lines[guardLocation[0]][guardLocation[1]+1:]
        if guardLocation[1]!=0:
            guardLocation[1]-=1
        else:
            return -1
        lines[guardLocation[0]] = lines[guardLocation[0]][:guardLocation[1]] + "<" + lines[guardLocation[0]][guardLocation[1]+1:]

notOut = True
while notOut:
    if checkMoveRotate(guardDir)==-1:
        notOut = False
    for line in lines:
        print(line)
    print("------------------------------------")