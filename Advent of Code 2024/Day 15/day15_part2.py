def get_robot_position(map):
    for i, row in enumerate(map):
        for j, clm in enumerate(row):
            if clm == "@": return (i, j)

def pretty_print(map):
    for m in map: 
        print("".join(m))

def get_positions(map, main_positions, direct):
    positions = []

    for main_position in main_positions:
        if not main_position in positions:
            positions.append(main_position)

        (x, y) = main_position

        if direct == (0, -1) or direct == (0, 1):
            nx, ny = x + direct[0], y + direct[1]
            if map[nx][ny] in {"[", "]"}:
                positions.append((nx, ny))
                main_positions.append((nx, ny))
        elif direct == (1, 0) or direct == (-1, 0): 
            if map[x][y] == "[":
                if map[x][y+1] == "]" and not (x, y+1) in positions:
                    positions.append((x, y + 1))
                    main_positions.append((x, y + 1))
            elif map[x][y] == "]":
                if map[x][y-1] == "[" and not (x, y-1) in positions:
                    positions.append((x, y - 1))
                    main_positions.append((x, y - 1))
            
            nx, ny = x + direct[0], y + direct[1]
            if map[nx][ny] in {"]", "["}:
                positions.append((nx, ny))
                main_positions.append((nx, ny))

    return positions

def make_moves(input, moves):
    map = [list(row) for row in input.split("\n")]
    m = 0
    for move in moves:
        print("I: " + str(m) + "/" + str(len(moves)) + " " + move)
        x, y = get_robot_position(map)

        if move == "<": direct = (0, -1)
        elif move == "^": direct = (-1, 0)
        elif move == ">": direct = (0, 1)
        elif move == "v": direct = (1, 0)

        next_x, next_y = x + direct[0], y + direct[1]
        next_char = map[next_x][next_y]
        if next_char == ".":
            map[next_x][next_y] = map[x][y]
            map[x][y] = "."
        elif next_char in {"[", "]"}:
            positions = sorted(get_positions(map, [(next_x, next_y)], direct))
            check = True
            if direct == (0, -1): # <
                min_column = positions[0][1]
                for position in positions:
                    if position[1] < min_column:
                        min_column = position[1]
                if not map[next_x][min_column-1] == ".":
                    check = False

                if check:
                    for i, position in enumerate(positions):
                        (px, py) = position
                        map[px + direct[0]][py + direct[1]] = map[px][py]
                        if i == len(positions)-1: # last position
                            map[px][py] = map[x][y]
                            map[x][y] = "."

            elif direct == (0, 1): # >   
                max_column = positions[0][1]
                for position in positions:
                    if position[1] > max_column:
                        max_column = position[1]
                if not map[next_x][max_column+1] == ".":
                    check = False

                if check:
                    for i, position in enumerate(reversed(positions)):
                        (px, py) = position
                        map[px + direct[0]][py + direct[1]] = map[px][py]
                        if i == len(positions)-1: # last position
                            map[px][py] = map[px][py-1]
                            map[x][y] = "."

            elif direct == (1, 0): # v
                for position in positions:
                    (px, py) = position
                    if map[px+1][py] == "#":
                        check = False

                if check:
                    first_row = positions[0][0]
                    for i, position in enumerate(reversed(positions)):
                        (px, py) = position

                        map[px + direct[0]][py + direct[1]] = map[px][py]
                        if px == first_row:
                            if map[px-1][py] == "@":
                                map[px][py] = map[px-1][py]
                                map[px-1][py] = "."
                            else:
                                map[px][py] = "."
                        else:
                            if (px - 1, py) not in positions:
                                map[px][py] = "."


            elif direct == (-1, 0): # ^
                for position in positions:
                    (px, py) = position
                    if map[px-1][py] == "#":
                            check = False

                if check:
                    last_row = positions[-1][0]
                    for position in positions:
                        (px, py) = position
                        map[px + direct[0]][py + direct[1]] = map[px][py]
                        if px == last_row:
                            map[px + direct[0]][py + direct[1]] = map[px][py]
                            if map[px+1][py] == "@":
                                map[px][py] = map[px+1][py]
                                map[px+1][py] = "."
                            else:
                                map[px][py] = "."
                        else:
                            if (px + 1, py) not in positions:
                                map[px][py] = "."
        m += 1
    return map

def get_GPS(map):
    gps = 0
    for i, row in enumerate(map):
        for j, clm in enumerate(row):
            if clm == "[":
                gps += 100 * i + j
    return gps

def make_bigger_map(map):
    return map.replace("#", "##").replace(".", "..").replace("@", "@.").replace("O", "[]")

file_name = 'input.txt'
#file_name = 'test_input3.txt'
#file_name = 'test_input.txt'

with open(file_name, 'r') as file:
    input = file.read()

map, moves = input.split("\n\n")
moves = moves.replace("\n","")
map = make_bigger_map(map)
map = make_moves(map, moves)
pretty_print(map)
result = get_GPS(map)
print("\nRESULT: " + str(result))