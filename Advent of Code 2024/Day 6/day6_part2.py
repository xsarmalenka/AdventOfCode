def get_guide_pos(lines):
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            if char in {"^", "v", ">", "<"}: 
                return i, j
    return None 

def get_guide_char(lines):
    pos = get_guide_pos(lines)
    if pos is not None:
        return lines[pos[0]][pos[1]]
    return None 

def move(lines):
    position = get_guide_pos(lines)
    if position is None: return lines
    
    position_row, position_column = position
    char = lines[position_row][position_column]
    new_lines = [list(row) for row in lines] 
    new_lines[position_row][position_column] = "X"

    if char == "^" and position_row > 0:
        next_char = lines[position_row - 1][position_column]
        if next_char != "#": new_lines[position_row - 1][position_column] = "^"
        else: new_lines[position_row][position_column + 1] = ">"
    elif char == ">" and position_column < len(lines[0]) - 1:
        next_char = lines[position_row][position_column + 1]
        if next_char != "#": new_lines[position_row][position_column + 1] = ">"
        else: new_lines[position_row + 1][position_column] = "v"
    elif char == "v" and position_row < len(lines) - 1:
        next_char = lines[position_row + 1][position_column]
        if next_char != "#": new_lines[position_row + 1][position_column] = "v"
        else: new_lines[position_row][position_column - 1] = "<"
    elif char == "<" and position_column > 0:
        next_char = lines[position_row][position_column - 1]
        if next_char != "#": new_lines[position_row][position_column - 1] = "<"
        else: new_lines[position_row - 1][position_column] = "^"

    return ["".join(row) for row in new_lines]

def finish(lines):
    position = get_guide_pos(lines)
    if position is None: return True
    position_row, position_column = position
    guide_char = lines[position_row][position_column]
    return (
        (guide_char == "^" and position_row == 0) or
        (guide_char == "v" and position_row == len(lines) - 1) or
        (guide_char == ">" and position_column == len(lines[0]) - 1) or
        (guide_char == "<" and position_column == 0)
    )

def simulate_guard_path(input_map):
    map_lines = input_map.strip().split("\n")
    while not finish(map_lines):
        map_lines = move(map_lines)

    position = get_guide_pos(map_lines)
    if position is not None:
        position_row, position_column = position
        map_lines[position_row] = map_lines[position_row][:position_column] + "X" + map_lines[position_row][position_column + 1:]

    return map_lines

def simulate_guard(input_map, obstruction_row, obstruction_column):
    map_lines = [list(row) for row in input_map.split("\n")]

    guide_pos = get_guide_pos(map_lines)
    if not(guide_pos == (obstruction_row, obstruction_column)):
        map_lines[obstruction_row][obstruction_column] = "0"
    
    visited_positions = set()
    loop_detected = False
    road = False

    while True:
        position_row, position_column = get_guide_pos(map_lines)
        current_char = map_lines[position_row][position_column]
        if current_char == ">" and position_column == len(map_lines[0])-1: break
        elif current_char == "v" and position_row == len(map_lines)-1: break
        elif current_char == "^" and position_row == 0: break
        elif current_char == "<" and position_column== 0: break

        if current_char in {"^", "v"}: visit = "|"
        elif current_char in {"<", ">"}: visit = "-"
        else: visit = current_char

        if road:
            map_lines[position_row][position_column] = "+"
            road = False
        else: map_lines[position_row][position_column] = visit
        
        # Pohyb strážce
        if current_char == "^" and position_row > 0:
            next_char = map_lines[position_row - 1][position_column]
            if next_char == "#" or next_char == "0":
                next_next_char = map_lines[position_row][position_column+1]
                if next_next_char == "0":
                    loop_detected = False
                    break
                else:
                    road = True
                    map_lines[position_row][position_column] = ">"
            elif next_char == "-":
                road = True
                map_lines[position_row - 1][position_column] = "^"
            elif next_char == "+":
                next_next_char = map_lines[position_row - 2][position_column]
                if next_next_char == ".":
                    map_lines[position_row][position_column - 1] = "^"
                else:
                    loop_detected = True
                    break
            else:
                map_lines[position_row - 1][position_column] = "^"
        elif current_char == "v" and position_row < len(map_lines) - 1:
            next_char = map_lines[position_row + 1][position_column]
            if next_char == "#" or next_char == "0":
                next_next_char = map_lines[position_row][position_column-1]
                if next_next_char == "0":
                    loop_detected = False
                    break
                else:
                    road = True
                    map_lines[position_row][position_column] = "<"
            elif next_char == "+":
                next_next_char = map_lines[position_row + 2][position_column]
                if next_next_char == ".":
                    map_lines[position_row][position_column - 1] = "v"
                else:
                    loop_detected = True
                    break
            elif next_char == "-":
                map_lines[position_row + 1][position_column] = "v"
            else:
                map_lines[position_row + 1][position_column] = "v"
        elif current_char == "<" and position_column > 0:
            next_char = map_lines[position_row][position_column - 1]
            if next_char == "#" or next_char == "0":
                next_next_char = map_lines[position_row-1][position_column]
                if next_next_char == "0":
                    loop_detected = False
                    break
                else:
                    road = True
                    map_lines[position_row][position_column] = "^"
            elif next_char == "|":
                road = True
                map_lines[position_row][position_column - 1] = "<"
            elif next_char == "+":
                next_next_char = map_lines[position_row][position_column - 2]
                if next_next_char == ".":
                    map_lines[position_row][position_column - 1] = "<"
                else:
                    loop_detected = True
                    break
            else:
                map_lines[position_row][position_column - 1] = "<"
        elif current_char == ">" and position_column < len(map_lines[0]) - 1:
            next_char = map_lines[position_row][position_column + 1]
            if next_char == "#" or next_char == "0":
                next_next_char = map_lines[position_row+1][position_column]
                if next_next_char == "0":
                    loop_detected = False
                    break
                else:
                    road = True
                    map_lines[position_row][position_column] = "v"
            elif next_char == "|":
                road = True
                map_lines[position_row][position_column + 1] = ">"
            elif next_char == "+":
                next_next_char = map_lines[position_row][position_column + 2]
                if next_next_char == ".":
                    map_lines[position_row][position_column + 1] = ">"
                else:
                    loop_detected = True
                    break
            else:
                map_lines[position_row][position_column + 1] = ">"

        if loop_detected: 
            break

        #if obstruction_row == 5 and obstruction_column == 6:
        #    for m in map_lines:
        #        print(m)

    map_lines = ["".join(row) for row in map_lines]
    return loop_detected


def find_obstruction_positions(input_map):
    map_with_path = simulate_guard_path(input_map)
    #print("MAP WITH PATH:")
    #print("\n".join(map_with_path))

    guide_path = [
        (i, j) for i, row in enumerate(map_with_path) for j, char in enumerate(row) if char == "X"
    ]

    result_counter = 0
    for row, column in guide_path:
        if simulate_guard(input_map, row, column): 
            result_counter += 1
            print(f"Loop detected at {row}, {column}") 

    return result_counter

# Main code
with open('input.txt', 'r') as file:
    input_map = file.read()

result = find_obstruction_positions(input_map)
print("RESULT:", result)
