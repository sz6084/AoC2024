## PART ONE ##
import pathlib, re

lines = pathlib.Path("exinput.txt").read_text().split("\n")

guardLocation = [-1,-1]
guardDir = "^"
symbols = ["^",">","v","<"]
for i in range(len(lines)):
    for j in range(len(lines[i])):
        symbol = lines[i][j]
        if symbol in symbols:
            guardLocation[0] = i
            guardLocation[1] = j
            guardDir = symbol

lines_copy = lines[:]
def checkMoveRotate(guardDir):
    # rotate symbols so less if statements? like a lazy susan?
    if (guardDir=="^" and lines[guardLocation[0]-1][guardLocation[1]]=="#"):
        lines_copy[guardLocation[0]][guardLocation[1]] = ">"
        guardDir = ">"
    else:
        lines[guardLocation[0]][guardLocation[1]] = "X"
        if guardLocation[0]!=0:
            guardLocation[0]-=1
        lines[guardLocation[0]][guardLocation[1]] = "^"
    if (guardDir==">" and lines[guardLocation[0]][guardLocation[1]+1]=="#"):
        lines_copy[guardLocation[0]][guardLocation[1]] = "v"
        guardDir = "v"
    else:
        lines[guardLocation[0]][guardLocation[1]] = "X"
        if guardLocation[1]!=len(lines[0])-1:
            guardLocation[1]+=1
        lines[guardLocation[0]][guardLocation[1]] = "v"
    if (guardDir=="v" and lines[guardLocation[0]+1][guardLocation[1]]=="#"):
        lines_copy[guardLocation[0]][guardLocation[1]] = "<"
        guardDir = "<"
    else:
        lines[guardLocation[0]][guardLocation[1]] = "X"
        if guardLocation[0]!=len(lines)-1:
            guardLocation[0]+=1
        lines[guardLocation[0]][guardLocation[1]] = "v"
    if (guardDir=="<" and lines[guardLocation[0]][guardLocation[1]-1]=="#"):
        lines_copy[guardLocation[0]][guardLocation[1]] = "^"
        guardDir = "^"
    else:
        lines[guardLocation[0]][guardLocation[1]] = "X"
        if guardLocation[1]!=0:
            guardLocation[1]-=1
        else:
            return -1
        lines[guardLocation[0]][guardLocation[1]] = "<"

notOut = True
while notOut:
    if checkMoveRotate(guardDir)==-1:
        notOut = False
    print(lines)