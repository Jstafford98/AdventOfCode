from itertools import combinations

def in_bounds(x : int, y : int, data : list[list]) -> bool :
    return 0 <= x < len(data[0]) and 0 <= y < len(data)

def generate_antinodes(
    p1 : tuple[int, int], p2 : tuple[int, int]
) -> tuple[tuple[int, int], tuple[int, int]] :
    x,y = p2[0] - p1[0], p2[1] - p1[1]
    return (p1[0] - x, p1[1] - y), (p2[0] + x, p2[1] + y)

if __name__ == '__main__' :
    
    #pt 1: 321 - too high, 318 - correct
    #pt 2: 1126 - correct
    with open("2024/day_eight/input.txt") as buff:
        data : list[str] = buff.read().splitlines()

    tower_map = dict()
    for y,line in enumerate(data):
        for x,c in enumerate(line):
            if not c.isalnum(): continue
            if c in tower_map: tower_map[c].append((x,y))
            else: tower_map[c] = [(x,y)]

    antinodes = set()
    for frequency, towers in tower_map.items():
        for vector in combinations(towers, r=2):
            for n in generate_antinodes(*vector):
                if in_bounds(*n, data): antinodes.add(n)
    print(len(antinodes))

    antinodes = set()
    for frequency, towers in tower_map.items():
        for p1, p2 in combinations(towers, r=2):
            point_found = True
            x,y = (p2[0] - p1[0], p2[1] - p1[1])
            while point_found:
                point_found = False
                p1, p2 =  (p1[0] - x, p1[1] - y), (p2[0] + x, p2[1] + y)
                if in_bounds(*p1, data):
                    point_found = True
                    antinodes.add(p1)
                if in_bounds(*p2, data):
                    point_found = True
                    antinodes.add(p2)

        for x in towers:
            antinodes.add(x)
    print(len(antinodes))