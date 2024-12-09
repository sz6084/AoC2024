## PART ONE ##
import pathlib

lines = pathlib.Path("exinput.txt").read_text().split("\n")

nums = []
for line in lines:
    line = line.split("|")
    nums = line
list(map(int, nums))