def check_east(text, row, column):
    if column < len(message_list[row])-1: 
        search = message_list[row][column+1]
        if search == text: 
            if text == "M":
                if not check_east("A", row, column+1): return 0
            elif text == "A":
                if not check_east("S", row, column+1): return 0
            return 1
        else: return 0
    else: return 0

def check_west(text, row, column):
    if column > 0:
        search = message_list[row][column-1]
        if search == text: 
            if text == "M":
                if not check_west("A", row, column-1): return 0
            elif text == "A":
                if not check_west("S", row, column-1): return 0
            return 1
        else: return 0
    else: return 0

def check_north(text, row, column):
    if row > 0:
        search = message_list[row-1][column]
        if search == text:
            if text == "M":
                if not check_north("A", row-1, column): return 0
            elif text == "A":
                if not check_north("S", row-1, column): return 0
            return 1
        else: return 0 
    else: return 0

def check_south(text, row, column):
    if row < len(message_list)-1:
        search = message_list[row+1][column]
        if search == text:
            if text == "M":
                if not check_south("A", row+1, column): return 0
            elif text == "A":
                if not check_south("S", row+1, column): return 0
            return 1
        else: return 0 
    else: return 0

def check_northeast(text, row, column):
    if row > 0 and column < len(message_list[row])-1:
        search = message_list[row-1][column+1]
        if search == text:
            if text == "M":
                if not check_northeast("A", row-1, column+1): return 0
            elif text == "A":
                if not check_northeast("S", row-1, column+1): return 0
            return 1
        else: return 0 
    else: return 0

def check_northwest(text, row, column):
    if row > 0 and column > 0:
        search = message_list[row-1][column-1]
        if search == text:
            if text == "M":
                if not check_northwest("A", row-1, column-1): return 0
            elif text == "A":
                if not check_northwest("S", row-1, column-1): return 0
            return 1
        else: return 0 
    else: return 0

def check_southeast(text, row, column):
    if row < len(message_list)-1 and column < len(message_list[row])-1:
        search = message_list[row+1][column+1]
        if search == text:
            if text == "M":
                if not check_southeast("A", row+1, column+1): return 0
            elif text == "A":
                if not check_southeast("S", row+1, column+1): return 0
            return 1
        else: return 0 
    else: return 0

def check_southwest(text, row, column):
    if row < len(message_list)-1 and column > 0:
        search = message_list[row+1][column-1]
        if search == text:
            if text == "M":
                if not check_southwest("A", row+1, column-1): return 0
            elif text == "A":
                if not check_southwest("S", row+1, column-1): return 0
            return 1
        else: return 0 
    else: return 0

with open('input.txt', 'r') as file:
    message = file.read()

message_list = [list(row) for row in message.splitlines()]
result = 0
for row in range(len(message_list)):
    for column in range(len(message_list[row])):
        if message_list[row][column] == "X":
            result += check_east("M", row, column)
            result += check_west("M", row, column)
            result += check_north("M", row, column)
            result += check_south("M", row, column)
            result += check_northeast("M", row, column)
            result += check_northwest("M", row, column)
            result += check_southeast("M", row, column)
            result += check_southwest("M", row, column)

print("RESULT: " + str(result))

