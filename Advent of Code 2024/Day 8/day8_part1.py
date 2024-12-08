from itertools import product

def find_frequencies(input):
    f_list = []
    for item in input:
        if not item in {".", "", "\n"} and not item in f_list: f_list.append(item)
    return f_list

def find_frequence_positions(input, frequence):
    positions = []
    map = input.split("\n")
    for i, row in enumerate(map):
        for j, clm in enumerate(row):
            if clm == frequence: positions.append([i, j])
    return positions

def add_antinode(antinodes, row, clm,):
    global limit
    position = [row, clm]
    if row >= 0 and clm >= 0 and row < limit and clm < limit:
        if not position in antinodes: antinodes.append(position)
    return antinodes

def find_antinodes(positions):
    antinodes = []
    all_combinations = product(positions, repeat=2)
    for ops in all_combinations:
        first_ops = ops[0]
        second_ops = ops[1]

        if first_ops != second_ops: 
            first_ops_row = first_ops[0]
            first_ops_clm = first_ops[1]
            second_ops_row = second_ops[0]
            second_ops_clm = second_ops[1]

            antinode_row = first_ops_row + (first_ops_row - second_ops_row)
            antinode_clm = first_ops_clm + (first_ops_clm - second_ops_clm)
            antinodes = add_antinode(antinodes, antinode_row, antinode_clm)

            antinode_row = second_ops_row - (first_ops_row - second_ops_row)
            antinode_clm = second_ops_clm - (first_ops_clm - second_ops_clm)
            antinodes = add_antinode(antinodes, antinode_row, antinode_clm)

    return antinodes

def draw_antinodes(map, positions):
    global result
    global test_antinodes
    new_map = map.split("\n") 
    new_map = [list(row) for row in new_map]
    
    for position in positions:
        x, y = position  
        current_char = new_map[x][y]
                
        if current_char == ".": 
            new_map[x][y] = "#"  
            test_antinodes.append([position, "."])
        elif current_char.isalnum(): 
            result += 1 
            test_antinodes.append([position, "a"])

    new_map = "\n".join("".join(row) for row in new_map)
    return new_map

def count_antinodes(map):
    counter = 0
    for item in map:
        if item == "#": counter += 1
    return counter

# Main program  
with open('input.txt', 'r') as file:
    input = file.read()

global result
global limit
global test_antinodes
result = 0
limit = len(input.split("\n"))
test_antinodes = []

frequence_list = find_frequencies(input)
map = input
for frequence in frequence_list:
    frequence_positions = find_frequence_positions(map, frequence)
    antinodes_positions = find_antinodes(frequence_positions) 
    antinode_map = draw_antinodes(map, antinodes_positions)
    map = antinode_map

# print(antinode_map)
result += count_antinodes(map)
print("RESULT: " + str(result))

dupliciter = 0
for test in test_antinodes:
    test_count = 0
    for test2 in test_antinodes:
        if test[0] == test2[0]:
            test_count += 1

            if test_count > 1: dupliciter += 1

dupliciter = dupliciter // 2
print("\nRESULT AFTER DUPLICITY REMOVER")
print(result-dupliciter)





