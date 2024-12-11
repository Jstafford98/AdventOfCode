UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
MOVEMENTS = [UP, DOWN, LEFT, RIGHT]

def tsum(t1 : tuple[int], t2 : tuple[int]) -> tuple[int] :
    return tuple(x + y for x,y in zip(t1, t2))

def dfs(arr: list[list[int]], start: tuple[int, int]):

    def _in_bounds(point: tuple[int, int]) -> bool:
        return 0 <= point[0] < len(arr[0]) and 0 <= point[1] < len(arr)

    def _neighbor_search(point: tuple[int, int], path: list[tuple[int, int]], visits: set[tuple[int, int]]):

        point_value = arr[point[1]][point[0]]

        for direction in MOVEMENTS:

            neighbor_p = tsum(point, direction)

            if not _in_bounds(neighbor_p) or neighbor_p in visits:
                continue

            neighbor_value = arr[neighbor_p[1]][neighbor_p[0]]
            if neighbor_value - point_value == 1:
                visits.add(neighbor_p)
                path.append(neighbor_p)
                yield from _neighbor_search(neighbor_p, path, visits)
                path.pop()
                visits.remove(neighbor_p)

        yield path[:]

    yield from _neighbor_search(start, [start], {start})


if __name__ == '__main__' :

    with open("2024/day_ten/input.txt") as buff:
        data : list[str] = [
            [int(x) for x in y] 
            for y in buff.read().splitlines()
        ]

    potential_trailheads : list[tuple[int, int]] = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == 0 :
                potential_trailheads.append((x,y))

    trails = dict()
    trailheads = dict()
    for t in potential_trailheads:
        for path in dfs(data, t):
            e = path[-1]
            if data[e[1]][e[0]] == 9:
                if path[0] in trailheads:
                    trailheads[path[0]].add(e)
                    trails[path[0]].add(tuple(path))
                else:
                    trailheads[path[0]] = {e,}
                    trails[path[0]] = {tuple(path),}

    total = 0
    for k,v in trailheads.items():
        total += len(v)
    print("Score Sum:", total)

    total = 0
    for k,v in trails.items():
        total += len(v)
    print("Rating Sum:", total)


            
