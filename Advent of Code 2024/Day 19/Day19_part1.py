from collections import deque

def sort_towels(towels, patterns):
    result = 0
    combinations = {}
    patterns = patterns.split("\n")
    i = 0
    for pattern in patterns:
        print("PATTERN " + pattern + " " + str(i) + "/" + str(len(patterns)))
        if can_construct_pattern(towels, pattern):
            result += 1
        i += 1

    return result

def can_construct_pattern(towels, pattern):
    towels = towels.split(", ")
    queue = deque([(0, towels)]) 
    visited = set() 

    while queue:
        i, available_towels = queue.popleft()

        if i == len(pattern):  
            return True

        available_towels_tuple = tuple(available_towels)

        if (i, available_towels_tuple) in visited:
            continue  
        visited.add((i, available_towels_tuple)) 

        for towel in available_towels:
            if pattern[i:i+len(towel)] == towel:
                new_towels = available_towels[:]  
                queue.append((i + len(towel), new_towels))

    return False 


file_name = 'input.txt'
#file_name = 'test_input.txt'

with open(file_name, 'r') as file:
    input = file.read()

towels, patterns = input.split("\n\n")
result = sort_towels(towels, patterns)
print("\nRESULT: " + str(result))