import re
from operator import mul

if __name__ == '__main__' :

    with open("2024/day_three/input.txt", "r") as buff:
        data = buff.read()

    total = 0
    for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)", data):
        total += mul(*(int(x) for x in re.findall(r"\d{1,3}", match)))
    print("Part One:", total)

    total = 0
    disabled = False
    for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data):
        if match == 'do()':
            disabled = False
        elif match == "don't()":
            disabled = True
        elif not disabled and (substr := re.match(r"mul\(\d{1,3},\d{1,3}\)", match)):
            total += mul(*(int(x) for x in re.findall(r"\d{1,3}", substr.string)))
    print("Part Two:", total)