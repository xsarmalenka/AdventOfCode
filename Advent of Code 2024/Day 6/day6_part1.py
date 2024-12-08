def get_guide_pos(lines):
    guide_pos = "[]"
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if not "#" in lines[i][j] and not "." in lines[i][j] and not "X" in lines[i][j]:
                guide_pos = "[" + str(i) + "," + str(j) + "]"
                break
    return guide_pos

def get_char_map(lines, row, column):
    return lines[row][column]

def set_map(lines, row, column, char):
    map = [[0 for i in range(len(lines))] for j in range(len(lines[0]))]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if i == row and j == column:
                map[i][j] = char
            else: 
                map[i][j] = lines[i][j]
    return map

def get_pos_row(lines):
    pos = get_guide_pos(lines)
    pos_row = int(pos.split(",")[0].replace("[", ""))
    return pos_row

def get_pos_column(lines):
    pos = get_guide_pos(lines)
    pos_column = int(pos.split(",")[1].replace("]", ""))
    return pos_column

def move(lines):
    map = lines
    position_row = get_pos_row(lines)
    position_column = get_pos_column(lines)
    char = get_char_map(lines, position_row, position_column)

    if char == "^" and position_row > 0:
        if get_char_map(map, position_row-1, position_column) != "#":
            #print("jdu nahoru")
            map = set_map(map, position_row, position_column, "X")
            map = set_map(map, position_row-1, position_column, "^")
        else:
            #print("nahore je prekazka")
            map = set_map(map, position_row, position_column, "X")
            map = set_map(map, position_row, position_column+1, ">")
    elif char == ">" and position_column < len(lines[0]):
        if get_char_map(map, position_row, position_column+1) != "#":
            #print("jdu doprava")
            map = set_map(map, position_row, position_column, "X")
            map = set_map(map, position_row, position_column+1, ">")
        else: 
            #print("vpravo je prekazka")
            map = set_map(map, position_row, position_column, "X")
            map = set_map(map, position_row+1, position_column, "v")
    elif char == "v" and position_row < len(lines):
            if get_char_map(map, position_row+1, position_column) != "#":
                #print("jdu dolu")
                map = set_map(map, position_row, position_column, "X")
                map = set_map(map, position_row+1, position_column, "v")
            else: 
                #print("dole je prekazka")
                map = set_map(map, position_row, position_column, "X")
                map = set_map(map, position_row, position_column-1, "<")
    elif char == "<" and position_column > 0:
        if get_char_map(map, position_row, position_column-1) != "#":
            #print("jdu doleva")
            map = set_map(map, position_row, position_column, "X")
            map = set_map(map, position_row, position_column-1, "<")
        else: 
            #print("vlevo je prekazka")
            map = set_map(map, position_row, position_column, "X")
            map = set_map(map, position_row-1, position_column, "^")
    return map 

def finish(lines):
    finish = False
    row = get_pos_row(lines)
    column = get_pos_column(lines)
    guide_char = get_char_map(lines, row, column)
    if guide_char == "^" and row == 0:
        finish = True
    elif guide_char == "v" and row == len(lines)-1:
        finish = True
    elif guide_char == ">" and column == len(lines[0])-1:
        finish = True
    elif guide_char == "<:" and column == 0:
        finish = True

    return finish

with open('input.txt', 'r') as file:
    input_map = file.read()
map_lines = input_map.split("\n")

while finish(map_lines) == False:
    map_lines = move(map_lines)

# secti X
result = 0 
for i in range(len(map_lines)):
    for j in range(len(map_lines[0])):
        char = get_char_map(map_lines, i, j)
        if char == "X":
            result += 1

print("RESULT: " + str(result+1))

