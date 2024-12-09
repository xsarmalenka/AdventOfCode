def get_block(input):
    block = []
    number_item = 0

    for i, item in enumerate(input):
        
        if i % 2 == 0: 
            number_item += 1
            block_item = number_item - 1
        else: 
            block_item = "."

        for j in range(int(item)): block.append(block_item)

    return block

def contains_non_dot(block, start_index):
    for item in block[start_index:]:
        if item != ".": return True
    return False

def sort_block(block):
    test_block = list(block)
    last_index_to_move = 0

    for i, item in enumerate(test_block):
        move = True
        if item == ".":
            if last_index_to_move == 0: index_item_to_move = len(test_block)-1
            else: last_index_to_move -= 1

            item_to_move = test_block[index_item_to_move]
            move = contains_non_dot(test_block, i)
            if move == True:
                while(item_to_move == "."):
                    index_item_to_move -= 1
                    item_to_move = test_block[index_item_to_move]

                test_block[i] = item_to_move
                test_block[index_item_to_move] = "."
                if last_index_to_move == 0:
                    last_index_to_move = index_item_to_move
            else: break

    return test_block

def get_check_sum(block):
    result = 0
    for i in range(len(block)):
        block_item = block[i]
        if block_item != ".":
            result += int(block_item) * i
    return result

# Main program  
#file_name = 'test_input_short.txt'
#file_name = 'test_input.txt'
file_name = 'input.txt'
#file_name = 'test_input_long.txt'

with open(file_name, 'r') as file:
    input = file.read()

block = get_block(input)
sorted_block = sort_block(block)
result = get_check_sum(sorted_block)
print("\nRESULT:\n" + str(result))

