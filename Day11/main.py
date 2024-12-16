## PART ONE ##
import pathlib, functools

line = pathlib.Path("input.txt").read_text().split()
line = [int(dig) for dig in line]
line_copy = line[:]

# initial solution, but recursion can be used for this part too
for i in range(25):
    j = 0
    while j<len(line):
        strElem = str(line[j])
        if line[j]==0:
            line[j]=1
        elif len(strElem)%2==0:
            line.insert(j,int(strElem[:len(strElem)//2]))
            line[j+1]=int(strElem[len(strElem)//2:])
            j+=1
        else:
            line[j]*=2024
        j+=1
print(len(line)) # run time is a few seconds

## PART TWO ##

@functools.cache
def blink(stone, remain):
    strElem = str(stone)
    if remain==0:
        return 1
    if stone==0:
        return blink(1, remain-1)
    elif len(strElem)%2==0:
        return blink(int(strElem[:len(strElem)//2]), remain-1) + blink(int(strElem[len(strElem)//2:]), remain-1)
    else:
        return blink(stone*2024, remain-1)
    return 1
j = 0
total = 0

while j<len(line_copy):
    total+=blink(line_copy[j], 75)
    j+=1
print(total)