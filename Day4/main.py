## PART ONE ##
import pathlib, re

lines = pathlib.Path("input.txt").read_text().split("\n")

total = 0

def check(lines):
    total_inner = 0
    for line in lines:
        matches = re.findall(r'(?=(XMAS))', line)
        matches += re.findall(r'(?=(SAMX))', line)
        total_inner+=len(matches)
    return total_inner

#horizontal
total+=check(lines)
print("horizontal:",total)

#vertical
lines_transposed = list(map(''.join, zip(*lines)))
total+=check(lines_transposed)
print("horizontal+vertical:",total)

#diag1
lines_copy = lines[:]
for i in range(len(lines_copy)):
    lines_copy[i] = i*""+lines_copy[i]+""*(len(lines_copy[i]) - i)
total+=check(lines_copy)
print("horizontal+vertical+diag1:",total)

#diag2
lines_copy = lines[:]
for i in range(len(lines_copy)):
    lines_copy[i] = ""*(len(lines_copy) - i)+lines_copy[i]+i*""
total+=check(lines_copy)
print("horizontal+vertical+diag1+diag2:",total)
#print(total)