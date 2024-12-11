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
        if not (x, y) in visited: visited.add((x, y))

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
    return len(visited)

#file_name = 'test_input2.txt'
# file_name = 'test_input.txt'
file_name = 'input.txt'

with open(file_name, 'r') as file:
    input = file.read()

result = move(input)
print("\nRESULT: " + str(result))