from collections import deque

def visualizate(input, bytes_count):
    map = list([["." for _ in range(max_range+1)] for _ in range(max_range+1)])

    lines = input.split("\n")
    for i in range(bytes_count):
        line = lines[i]
        x = int(line.split(",")[1])
        y = int(line.split(",")[0])
        map[x][y] = "#"
    return map

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

if file_name == 'test_input.txt': max_range = 6
elif file_name == 'input.txt': max_range = 70

start_position = (0,0)
end_position = (max_range, max_range)
count_steps = 0
i = 0

while not count_steps == -1:
    map = visualizate(input, i)
    steps = go_to_end(map)
    count_steps = len(steps)-1
    i += 1
    
print("\nRESULT: " + input.split("\n")[i-2])
