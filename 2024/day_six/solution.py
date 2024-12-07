from itertools import cycle, chain

GUARD = '^'
OBSTACLE = '#'
DIRECTION_SET : list[tuple[int, int]] = [
    (0, -1), (1, 0), (0, 1), (-1, 0)] # UP, RIGHT, DOWN, LEFT

def locate_guard(data : list[list[str]]) -> tuple[int, int] :
    ''' returns position of guard as an x,y coordinate '''
    for y, line in enumerate(data):
        try:
            x = line.index(GUARD)
            return (x,y)
        except ValueError:
            continue
    else:
        raise Exception("No guard found in the data.")

def calculate_path(arr : list[list[str]]):
    ''' determines the path the guard will take to exit the room '''
    directions = cycle(DIRECTION_SET)
    direction = next(directions)

    # locate guard
    guard_position = locate_guard(arr)

    total_revisits = 0
    visitable_cells = sum(1 for cell in chain(*arr) if cell != OBSTACLE)
    visits : set[tuple[tuple[int, int], tuple[int, int]]] = set()
    path_valid = True

    while True:

        # log our cell visit
        visit = guard_position, direction
        if visit in visits: 
            total_revisits += 1
        visits.add(visit)

        next_x, next_y = map(sum, zip(guard_position, direction))

        if not (0 <= next_x < len(arr[0]) and 0 <= next_y < len(arr)):
            # next step would be out of bounds
            break
        
        if total_revisits > visitable_cells:
            # the guard has revisited cells more than it's found new ones
            path_valid = False
            break

        if arr[next_y][next_x] == OBSTACLE:
            # guard turns if next position is an obstacle 
            direction = next(directions)
            continue
        
        # guard moves to next position if valid move
        guard_position = next_x, next_y
    
    return visits, path_valid

if __name__ == '__main__' :
    
    with open("2024/day_six/input.txt") as buff:
        data : list[list[str]] = buff.readlines()

    guard_path, valid = calculate_path(data)
    unique_positions = set(position for position, _ in guard_path)
    print("Part One: ", len(unique_positions))

    guard_initial_position = locate_guard(data)
    guard_second_position = tuple(map(sum, zip(guard_initial_position, DIRECTION_SET[0])))

    blocks = 0
    for position in unique_positions:
        if position == guard_initial_position or position == guard_second_position:
            continue
        data_copy = [[y for y in x] for x in data]
        data_copy[position[1]][position[0]] = OBSTACLE
        path, valid = calculate_path(data_copy)
        if not valid:
            blocks += 1
    print("Part Two: ", blocks)
