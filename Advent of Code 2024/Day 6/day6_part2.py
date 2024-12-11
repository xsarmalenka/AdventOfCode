from collections import Counter

def pretty_print(map):
    for m in map:
        print(m)

def get_position(map, char):
    for i, row in enumerate(map):
        for j, clm in enumerate(row):
            if clm in char:
                return (i, j)
    return None

def go_out(map, guard_position, visited):
    x = guard_position[0]
    y = guard_position[1]
    guard_char = map[x][y]
    stop = False

    while not stop:
        if not (x, y) in visited: 
            if not (x, y) == (guard_position[0], guard_position[1]):
                visited.add((x, y))

        if guard_char == "^": direct = (-1, 0)
        elif guard_char == ">": direct = (0, 1)
        elif guard_char == "<": direct = (0, -1)
        elif guard_char == "v": direct = (1, 0)

        dx = direct[0]
        dy = direct[1]
        nx, ny = x + dx, y + dy

        if nx == len(map) and guard_char == "v": stop = True
        if nx == 0-1 and guard_char == "^": stop = True
        if ny == len(map) and guard_char == ">": stop = True
        if ny == 0-1 and guard_char == "<": stop = True

        if not stop:
            if map[nx][ny] != "#":   
                x = nx
                y = ny
            else: # change direct
                if guard_char == "^": guard_char = ">"
                elif guard_char == ">": guard_char = "v"
                elif guard_char == "<": guard_char = "^"
                elif guard_char == "v": guard_char = "<"

    return visited

def move(input):
    map = list(input.split("\n")) 
    guard_pos = get_position(map, {"<", ">", "v", "^"})
    visited = set()
    visited = go_out(map, guard_pos, visited)
    return visited

def go(map, guard_position, trace):
    x = guard_position[0]
    y = guard_position[1]
    guard_char = map[x][y]
    stop = False
    trace_counter = Counter()
    loop = 0
    is_loop = False

    plus_trace_counter = Counter()
    plus_trace = set()

    while not stop: 
        if guard_char == "^": direct = (-1, 0)
        elif guard_char == ">": direct = (0, 1)
        elif guard_char == "<": direct = (0, -1)
        elif guard_char == "v": direct = (1, 0)

        if trace_counter[(x,y)] >= 2:
            plus_trace.add((x,y))
            plus_trace_counter[(x,y)] += 1

        if plus_trace_counter[(x,y)] >= 2:
            loop += 1
        
        if loop == 2:
            is_loop = True
            stop = True

        trace.add((x, y))
        trace_counter[(x,y)] += 1

        dx = direct[0]
        dy = direct[1]
        nx, ny = x + dx, y + dy

        if nx == len(map) and guard_char == "v": stop = True
        if nx == -1 and guard_char == "^": stop = True
        if ny == len(map) and guard_char == ">": stop = True
        if ny == -1 and guard_char == "<": stop = True

        if not stop:
            if map[nx][ny] != "#":   
                x = nx
                y = ny
            else: # change direct
                if guard_char == "^": guard_char = ">"
                elif guard_char == ">": guard_char = "v"
                elif guard_char == "<": guard_char = "^"
                elif guard_char == "v": guard_char = "<"

    return is_loop

def find_loop(input, visited):
    #for visit in visited:
    count = 0
    for i, visit in enumerate(visited):
        #if i == 0: # test
        print(str(visit) + " I: " + str(i) + "/" + str(len(visited)))
        map = [list(line) for line in input.split("\n")]
        map[visit[0]][visit[1]]= "#"
        guard_pos = get_position(map, {"<", ">", "v", "^"})
        trace = set()
        loop = go(map, guard_pos, trace)
        #pretty_print(map)

        if loop: 
            count += 1
    return count

#file_name = 'test_input.txt'
file_name = 'input.txt'

with open(file_name, 'r') as file:
    input = file.read()

visited = move(input)
result = find_loop(input, visited)
print("\nRESULT: " + str(result))