## PART ONE ##
import pathlib
import re

p = r"mul\((\d+),(\d+)\)"
lines = pathlib.Path("input.txt").read_text()

#print(re.findall(p, lines))
total = 0
for a, b in re.findall(p, lines):
    total+=int(a)*int(b)
#print(total)

## PART TWO ##
total2 = 0
p_new = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
#print(re.findall(p_new, lines))
enabled = True
for a, b, do, dont in re.findall(p_new, lines):
    if dont:
        enabled = False
        #print("dont:", a, b)
    elif enabled and a and b:
        total2+=int(a)*int(b)
        #print("ints:", a, b)
    elif do:
        enabled = True
        #print(a, b)
print(total2)