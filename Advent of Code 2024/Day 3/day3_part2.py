import re

with open('input.txt', 'r') as file:
    message = file.read()

def get_instructions_result(start_index, end_index):
    result = 0
    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", message[start_index:end_index])
    for instruction in instructions:
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        sec_match = re.match(pattern, instruction)
        if sec_match:
            num1 = int(sec_match.group(1))
            num2 = int(sec_match.group(2))
            result += num1 * num2
    return result

matches = re.finditer(r"do\(\)|don't\(\)", message)
match_info = [(match.group(), match.start(), match.end()) for match in matches]
res = get_instructions_result(0, match_info[0][1])
for i in range(len(match_info)):
    current_match = match_info[i]

    if i == len(match_info)-1: next_match_start = len(message)
    else: next_match_start = match_info[i+1][1]

    current_match_start = current_match[1]
    if current_match[0] == "do()": res += get_instructions_result(current_match[1], next_match_start)

print("RESULT: " + str(res))
