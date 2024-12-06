NORTH = (1, 0)
SOUTH = (-1, 0)
EAST = (0, 1)
WEST = (0, -1)
NORTH_EAST = (1, 1)
SOUTH_EAST = (-1, 1)
SOUTH_WEST = (-1, -1)
NORTH_WEST = (1, -1)

diagonal_pairs = [(NORTH_EAST, SOUTH_WEST), (NORTH_WEST, SOUTH_EAST)]
directions = [NORTH, SOUTH, EAST, WEST, NORTH_EAST, SOUTH_EAST, SOUTH_WEST, NORTH_WEST]

if __name__ == '__main__':

    with open("2024/day_four/input.txt") as buff:
        data = buff.readlines()

    # Part 1
    search_depth = 4
    total_matches = 0
    for start_y in range(len(data)):
        for start_x in range(len(data[0])):
            for dir_y, dir_x in directions:
                result = ''
                x, y = start_x, start_y
                for _ in range(search_depth):
                    if x < 0 or x >= len(data[0]) or y < 0 or y >= len(data):
                        break
                    result += data[y][x]
                    y += dir_y
                    x += dir_x
                if result == 'XMAS':
                    total_matches += 1
    print(total_matches)

    # Part 2
    total_matches = 0
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            if (middle := data[y][x]) != 'A':
                continue
            results = []
            for ((dy1, dx1), (dy2, dx2)) in diagonal_pairs:
                try:
                    dp1, dp2 = data[y + dy1][x + dx1], data[y + dy2][x + dx2]
                    match = f"{dp1}{middle}{dp2}"
                    if match in {"MAS", "SAM"}:
                        results.append(match)
                except IndexError:
                    continue
            total_matches += 1 if len(results) == 2 else 0
    print(total_matches)