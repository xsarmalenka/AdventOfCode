def check(row, column):
    if row > 0 and column > 0 and column < len(message_list[row])-1 and row < len(message_list)-1:
        westnorth = message_list[row-1][column-1]
        westsouth = message_list[row+1][column-1]
        
        if (westnorth == "M" or westnorth == "S") and (westsouth == "M" or westsouth == "S"):
            eastnorth = message_list[row-1][column+1]
            eastsouth = message_list[row+1][column+1]
            if (eastnorth == "M" or eastnorth == "S") and (eastsouth == "M" or eastsouth == "S"):
                if (westnorth != eastsouth) and (eastnorth != westsouth):
                    return 1
                else: return 0
            else: return 0
        else: return 0
    else: return 0

with open('input2.txt', 'r') as file:
    message = file.read()

message_list = [list(row) for row in message.splitlines()]
result = 0
for row in range(len(message_list)-1):
    for column in range(len(message_list[row])-1):
        if message_list[row][column] == "A":
            result += check(row, column)

print("RESULT: " + str(result))

