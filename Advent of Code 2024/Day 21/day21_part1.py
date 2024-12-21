from itertools import permutations
from collections import deque

def pretty_print(input):
    for i in input:
        print(i)

def get_position(numeric_keyboard, char):
    for i, row in enumerate(numeric_keyboard):
        for j, clm in enumerate(row):
            if clm == char:
                return (i, j)

def get_keyboard_list(keyboard):
    lines = keyboard.split("\n")
    keypad = []

    for line in lines:
        if "|" in line:  
            row = [char.strip() if char.strip() else None for char in line.split("|")[1:-1]]
            if len(row) == 2:
                row = ['-', row[0], row[1]]
            keypad.append(row)

    keypad = [row for row in keypad if row]
    return keypad

def get_move(direct):
    if direct == (0, -1): return "<"
    elif direct == (-1, 0): return "^"
    elif direct == (0, 1):  return ">"
    elif direct == (1, 0): return "v"

def solver_xy(direct_diff, moves, axe, direct_position, check):
    if axe == "X":  
        if direct_diff[0] > 0: direct = (1, 0)
        elif direct_diff[0] < 0: direct = (-1, 0)
        direct_diff = (direct_diff[0] - direct[0], direct_diff[1])
    elif axe == "Y": 
        if direct_diff[1] > 0: direct = (0, 1)
        elif direct_diff[1] < 0: direct = (0, -1)
        direct_diff = (direct_diff[0], direct_diff[1] - direct[1])

    new_direct_position = (direct_position[0] + direct[0], direct_position[1] + direct[1])
    if new_direct_position == (3, 0):
        check = False

    moves.append(get_move(direct))
    return direct_diff, moves, new_direct_position, check

def solver_xy_direct(direct_diff, moves, axe, direct_position, check):
    if axe == "X":  
        if direct_diff[0] > 0: direct = (1, 0)
        elif direct_diff[0] < 0: direct = (-1, 0)
        direct_diff = (direct_diff[0] - direct[0], direct_diff[1])
    elif axe == "Y": 
        if direct_diff[1] > 0: direct = (0, 1)
        elif direct_diff[1] < 0: direct = (0, -1)
        direct_diff = (direct_diff[0], direct_diff[1] - direct[1])

    new_direct_position = (direct_position[0] + direct[0], direct_position[1] + direct[1])
    if new_direct_position == (0, 0):
        check = False

    moves.append(get_move(direct))
    return direct_diff, moves, new_direct_position, check

def generate_combinations(candidates_x, candidates_y):
    elements = ["X", "Y"]
    candidates_list = ["X"] * candidates_x + ["Y"] * candidates_y
    unique_combinations = set(permutations(candidates_list))
    return [list(comb) for comb in unique_combinations]

def enter_number(number, numeric_position, moves):
    global numeric_keyboard
    numeric_number_position = get_position(numeric_keyboard, str(number))
    direct_x = numeric_number_position[0] - numeric_position[0]
    direct_y = numeric_number_position[1] - numeric_position[1]
    direct_diff = (direct_x, direct_y)
    candidates = abs(direct_diff[0]) + abs(direct_diff[1])

    if candidates == 1:
        moves.append(get_move(direct_diff))
        moves.append("A")
        result_moves = ["".join(moves)]
    else:
        x_candidates = abs(direct_diff[0])
        y_candidates = abs(direct_diff[1])
        candidates_list = generate_combinations(x_candidates, y_candidates)
        mem_direct_diff = direct_diff
        mem_direct_pos = numeric_position
        result_moves = [] 
        check = True

        for candidate_list in candidates_list:
            temp_moves = moves.copy()  
            direct_diff = mem_direct_diff
            numeric_position = mem_direct_pos
            for i in range(len(candidate_list)):
                direct_diff, temp_moves, numeric_position, check = solver_xy(direct_diff, temp_moves, candidate_list[i], numeric_position, check)
            
            if check:
                temp_moves.append("A")  
                result_moves.append("".join(temp_moves))   
            else: check = True
            
    return result_moves, numeric_number_position

def enter_char(char, direct_position, moves):
    global direct_keyboard
    direct_char_position = get_position(direct_keyboard, char)
    direct_x = direct_char_position[0] - direct_position[0]
    direct_y = direct_char_position[1] - direct_position[1]
    direct_diff = (direct_x, direct_y)
    candidates = abs(direct_diff[0]) + abs(direct_diff[1])
    check = True

    if candidates == 1:
        moves.append(get_move(direct_diff))
        moves.append("A")
        result_moves = ["".join(moves)]
        direct_position = (direct_position[0] + direct_diff[0], direct_position[1] + direct_diff[1]) # test
    else:
        x_candidates = abs(direct_diff[0])
        y_candidates = abs(direct_diff[1])
        candidates_list = generate_combinations(x_candidates, y_candidates)
        mem_direct_diff = direct_diff
        mem_direct_pos = direct_position
        result_moves = [] 

        for candidate_list in candidates_list:
            temp_moves = moves.copy()  
            direct_diff = mem_direct_diff
            direct_position = mem_direct_pos
            for i in range(len(candidate_list)):
                direct_diff, temp_moves, direct_position, check = solver_xy_direct(direct_diff, temp_moves, candidate_list[i], direct_position, check)

            if check:
                temp_moves.append("A")  
                result_moves.append("".join(temp_moves))  
            else: check = True

    return result_moves, direct_char_position

def enter_the_code(code):
    numeric_position = get_position(numeric_keyboard, "A")
    direct_position = get_position(direct_keyboard, "A")

    current_moves = [""]  
    for number in code:
        next_moves = [] 
        help_num_pos = numeric_position
        for moves in current_moves:
            moves_list = list(moves) 
            result_moves, numeric_position = enter_number(number, help_num_pos, moves_list)
            next_moves.extend(result_moves) 
        current_moves = next_moves  
    return current_moves   

def enter_the_code_second(first_moves):
    direct_position = get_position(direct_keyboard, "A")
    
    sec_moves = set()
    for first_move in first_moves:
        second_moves = [""] 
        for char in first_move:
            next_moves = [] 
            help_dir_pos = direct_position
            for i, moves in enumerate(second_moves):
                moves_list = list(moves) 
                result_moves, direct_position = enter_char(char, help_dir_pos, moves_list)

                if i == 0:
                    next_moves.extend(result_moves) 
                    second_moves = next_moves 
                else:
                    second_moves.extend(result_moves)
        
        for second_move in second_moves:
            sec_moves.add(second_move)
    return sec_moves

global numeric_keyboard, direct_keyboard

file_name = 'input.txt'
#file_name = 'test_input.txt'

with open(file_name, 'r') as file:
    input = file.read()

with open('direct_keyboard.txt', 'r') as file:
    direct_keyboard = file.read()

with open('numeric_keyboard.txt', 'r') as file:
    numeric_keyboard = file.read()

numeric_keyboard = get_keyboard_list(numeric_keyboard)
direct_keyboard = get_keyboard_list(direct_keyboard)
codes = input.split("\n")
result = 0

for code in codes:
    first_moves = enter_the_code(code)
    second_moves = enter_the_code_second(first_moves)
    third_moves = enter_the_code_second(second_moves)

    min_code = min(third_moves, key=len)
    print(code + ": " + min_code)
    print(len(min_code))

    if code.startswith(str(0)): res_code = code[1:-1]
    else: res_code = code[0:-1]

    print(res_code)
    code_result = len(min_code) * int(res_code)
    result += code_result

print("\nRESULT: " + str(result))

