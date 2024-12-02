import pathlib

lines = pathlib.Path("exinput.txt").read_text().split("\n")

numSafe = 0
for line in lines:
    for i in range(3,len(line)):
        if(line[1]>line[0]):
            if(line[i+1]<line[i]):
                break
            print(line[i+1]+line[i])
            numSafe+=1
        else:
            if(line[i+1]>line[i]):
                break
            print(line[i+1]+line[i])
            numSafe+=1
print(numSafe)