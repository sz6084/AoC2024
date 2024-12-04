## PART ONE ##
import pathlib, re

lines = pathlib.Path("exinput.txt").read_text().split("\n")

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

#vertical
lines_transposed = list(map(''.join, zip(*lines)))
total+=check(lines_transposed)

lines_copy = lines[:]
for i in range(len(lines_copy)):
    lines_copy[i] = i*""+lines_copy[i]
total+=check(lines_copy)

lines_copy = lines[:]
for i in range(len(lines_copy)):
    lines_copy[i] = lines_copy[i]+i*""
total+=check(lines_copy)
print(total)