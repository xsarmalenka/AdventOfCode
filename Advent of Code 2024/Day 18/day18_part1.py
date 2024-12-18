from collections import deque

def pretty_print(map):
    for m in map:
        print("".join(m))

def visualizate(input):
    map = list([["." for _ in range(max_range+1)] for _ in range(max_range+1)])

    lines = input.split("\n")
    for i in range(bytes_count):
        line = lines[i]
        x = int(line.split(",")[1])
        y = int(line.split(",")[0])
        map[x][y] = "#"
    return map

def visualizate_steps(input, steps):
    
    for step in steps:
        x, y = step
        map[x][y] = "O"

    pretty_print(map)


def go_to_end(map):

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    visited = set()  
    queue = deque([(start_position, [])])  

    while queue:
        current_position, path = queue.popleft()
        x, y = current_position

        if current_position == end_position:
            return path + [current_position]

        if current_position not in visited:
            visited.add(current_position)
            
            for direction in directions:
                nx, ny = x + direction[0], y + direction[1]
                if 0 <= nx <= max_range and 0 <= ny <= max_range:  
                    if map[nx][ny] != "#" and (nx, ny) not in visited:
                        queue.append(((nx, ny), path + [current_position]))
    return [] 

file_name = 'input.txt'
#file_name = 'test_input.txt'

with open(file_name, 'r') as file:
    input = file.read()

if file_name == 'test_input.txt':
    max_range = 6
    bytes_count = 12
elif file_name == 'input.txt':
    max_range = 70
    bytes_count = 1024

start_position = (0,0)
end_position = (max_range, max_range)

map = visualizate(input)
steps = go_to_end(map)

visualizate_steps(map, steps)
print("\nRESULT: " + str(len(steps)-1))