from collections import deque

def sort_towels(towels, patterns):
    result = 0
    combinations = {}
    patterns = patterns.split("\n")
    i = 0
    for pattern in patterns:
        res = can_construct_pattern(towels, pattern)
        print("PATTERN " + pattern + " " + str(i) + "/" + str(len(patterns)) + " combinations: " + str(res))
        result += res
        i += 1

    return result

def can_construct_pattern(towels, pattern):
    towels = towels.split(", ")  
    n = len(pattern)
    
    dp = [0] * (n + 1)
    dp[0] = 1  
    
    for i in range(1, n + 1):
        for towel in towels:
            if i >= len(towel) and pattern[i - len(towel):i] == towel:
                dp[i] += dp[i - len(towel)]  

    return dp[n] 

file_name = 'input.txt'
#file_name = 'test_input.txt'

with open(file_name, 'r') as file:
    input = file.read()

towels, patterns = input.split("\n\n")
result = sort_towels(towels, patterns)
print("\nRESULT: " + str(result))