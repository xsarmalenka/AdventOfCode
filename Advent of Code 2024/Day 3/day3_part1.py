import re

with open('input.txt', 'r') as file:
    message = file.read()


instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", message)
result = 0 
for instruction in instructions:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    match = re.match(pattern, instruction)
    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(2))

        result += num1 * num2

print("RESULT: " + str(result))
