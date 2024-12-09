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

def find_dots_array(block, size):
    current_count = 0
    pos = -1

    for i, item in enumerate(block):
        if item == ".":
            current_count += 1
            if pos == -1:
                pos = i
        else:
            current_count = 0
            pos = -1
        
        if current_count == size: 
            break
        else: 
            if i == len(block)-1: pos = -1

    return pos

def find_index_from_end(arr, value):
    for i in range(len(arr) - 1, -1, -1): 
        if arr[i] == value: 
            return i
    return -1 

def make_move(block, index, count, number):
    for i in range(count):
        block[index+i] = number
        number_index = find_index_from_end(block, number)
        block[number_index] = "."
    return block

def sort_block(block):
    test_block = list(block)
    last_id = int(block[len(block)-1])
    for i in range(last_id, -1, -1):
        print("SORT: " + str(i))
        count_id_number = test_block.count(i)
        start_index = find_dots_array(test_block, count_id_number)
        if start_index > -1:
            test_block = make_move(test_block, start_index, count_id_number, i)
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

