## PART ONE ##
import pathlib

lines = pathlib.Path("input.txt").read_text().split("\n")
reports = []
numSafe = 0

for line in lines:
    reports.append(list(map(int, line.split())))

#def isSafe(report)->bool:
def isSafe(report):
    diffs=[]
    for i in range(1,len(report)):
        diffs.append(report[i]-report[i-1])
    for num in diffs:
        if diffs[0]>0 and num<0:
            return False
        elif diffs[0]<0 and num>0:
            return False
        if abs(num)>3 or num==0:
            return False
    return True
            
for report in reports:
    if isSafe(report):
        numSafe+=1
#print(numSafe)

## PART TWO ##
numSafe2 = 0
for report in reports:
    if isSafe(report):
        numSafe2+=1
    else:
        reportCopy = report[:]
        for i in range(len(reportCopy)):
            del reportCopy[i]
            if isSafe(reportCopy):
                numSafe2+=1
                break
            reportCopy = report[:]
print(numSafe2)