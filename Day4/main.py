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
print("horizontal:",total)

#vertical
total+=checkVertical(lines)
print("horizontal+vertical:",total)

#diag1
lines_copy = lines[:]
for i in range(len(lines_copy)):
    lines_copy[i] = i*"."+lines_copy[i]+"."*(len(lines_copy[i]) - i)
total+=checkVertical(lines_copy)
print("horizontal+vertical+diag1:",total)

#diag2
lines_copy = lines[:]
for i in range(len(lines_copy)):
    lines_copy[i] = "."*(len(lines_copy) - i)+lines_copy[i]+i*"."
total+=checkVertical(lines_copy)
print("horizontal+vertical+diag1+diag2:",total)
#print(total)