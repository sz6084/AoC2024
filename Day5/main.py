## PART ONE ##
import pathlib

lines = pathlib.Path("exinput.txt").read_text().split("\n")

nums = []
for line in lines:
    if "|" in line:
        nums+=line[:2]