def get_robot_position(map):
    for i, row in enumerate(map):
        for j, clm in enumerate(row):
            if clm == "@": return (i, j)

def pretty_print(map):
    for m in map: print("".join(m))

def make_moves(input, moves):
    map = [list(row) for row in input.split("\n")]
    x, y = get_robot_position(map)
    for move in moves: 
        if move == "<": direct_diff = (0, -1)
        elif move == "^": direct_diff = (-1, 0)
        elif move == ">": direct_diff = (0, 1)
        elif move == "v": direct_diff = (1, 0)
        else: break

        new_x = x + direct_diff[0]
        new_y = y + direct_diff[1]
        next_char = map[new_x][new_y]

        if next_char != "#":
            if next_char == ".":
                map[x][y] = '.'
                x = new_x
                y = new_y
                map[x][y] = "@"  
            elif next_char == "O":
                new_next_x = new_x + direct_diff[0]
                new_next_y = new_y + direct_diff[1]
                next_next_char = map[new_next_x][new_next_y]

                if next_next_char != "#":
                    if next_next_char == ".":
                        map[x][y] = '.'
                        x = new_x
                        y = new_y
                        map[x][y] = "@"
                        map[new_next_x][new_next_y] = "O"
                    elif next_next_char == "O":
                        new_next_next_x = new_next_x + direct_diff[0]
                        new_next_next_y = new_next_y + direct_diff[1]
                        next_next_next_char = map[new_next_next_x][new_next_next_y]
                        
                        boxes = 2
                        while(next_next_next_char not in {".", "#"}):
                            boxes += 1
                            new_next_next_x = new_next_next_x + direct_diff[0]
                            new_next_next_y = new_next_next_y + direct_diff[1]
                            next_next_next_char = map[new_next_next_x][new_next_next_y]
                        
                        if next_next_next_char == ".":
                            map[x][y] = '.'
                            x = new_x
                            y = new_y
                            map[x][y] = "@"
                            for box in range(1, boxes+1):
                                box_x = new_x + direct_diff[0]*box
                                box_y = new_y + direct_diff[1]*box
                                map[box_x][box_y] = "O"

    pretty_print(map)
    return map

def get_GPS(map):
    gps = 0
    for i, row in enumerate(map):
        for j, clm in enumerate(row):
            if clm == "O":
                gps += 100 * i + j
    return gps

file_name = 'input.txt'
#file_name = 'test_input.txt'
#file_name = 'test_input2.txt'

with open(file_name, 'r') as file:
    input = file.read()

map, moves = input.split("\n\n")
moves = moves.replace("\n","")
print(moves)
map = make_moves(map, moves)
result = get_GPS(map)
print("\nRESULT: " + str(result))