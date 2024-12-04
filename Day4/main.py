## PART ONE ##
import pathlib

lines = pathlib.Path("exinput.txt").read_text().split("\n")

total = 0

def findDiag(line, row):
    innerTotal = 0
    index = line.find("X")
    if (line.find("S")>0) and (line.find("S") < index):
        index = line.find("S")
    if index < -1:
        return 0
    if index > len(line)-4:
        return 0
    #print("rowb4run:",row)
    #print("indexb4run:",index)
    for i in range(index, len(line)-4):
        index = line.find("X", i)
        if line.find("S", i) < index:
            index = line.find("S", i)
        #print("ind=1",index+1)
        # back diag
        if row>len(lines)-4:
            return 0
        elif ("XMAS" in (lines[row][index] + lines[row+1][index+1] + lines[row+2][index+2] + lines[row+3][index+3])):
            innerTotal+=1
            # forward diag
        if row<3: # row index starts at 0
            return 0
        elif ("XMAS" in (lines[row-3][index-3] + lines[row-2][index-2] + lines[row-1][index-1] + lines[row][index])):
            innerTotal+=1
    return innerTotal

def findAcross(line):
    innerTotal = 0
    index = line.find("XMAS")
    if (line.find("SAMX")>0) and (line.find("SAMX") < index):
        index = line.find("SAMX")
    if index < -1:
        return 0
    innerTotal+=1
    for i in range(index+3, len(line)):
        index = line.find("XMAS", i)
        if (line.find("SAMX")>0) and (line.find("SAMX") < index):
            index = line.find("SMAX", i)
        if index>0:
            innerTotal+=1
        else:
            return 0
    return innerTotal

row = 0
for line in lines:
    #print(line)
    #index = line.find("XMAS")
    #revIndex = line.find("SAMX")
    #if index>0 or revIndex>0:
    #    total+=1
    total+=findAcross(line)
    total+=findDiag(line, row)
    row+=1
print(total)