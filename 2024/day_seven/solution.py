import re
from operator import mul, add
from itertools import product

def concat(a : int, b : int) -> int :
    return int(f'{a}{b}')

def evaluate(values : list[int], operators : list) -> int :
    result = values[0]
    for i,op in enumerate(operators, 1):
        result = op(result, values[i])
    return result

if __name__ == '__main__' :

    with open("2024/day_seven/input.txt") as buff:
        data = buff.readlines()
    #pt1 : 932137732557 - correct
    #pt2 : 661823605105500 - correct

    total = 0
    for line in data:
        result, *values = map(int, re.findall(r"(\d+)", line))
        for combo in product((mul, add), repeat=len(values) - 1):
            if evaluate(values, combo) == result:
                total += result
                break
    print(total)

    total = 0
    for line in data:
        result, *values = map(int, re.findall(r"(\d+)", line))
        for combo in product((mul, add, concat), repeat=len(values) - 1):
            if evaluate(values, combo) == result:
                total += result
                break
    print(total)
