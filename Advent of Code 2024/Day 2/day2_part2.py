def is_safe_line(line):
    levels = line.replace("\n", "").split(" ")
    asc = False
    desc = False
    safe = 0
    for i in range(len(levels)-1):
        number = int(levels[i])
        next_number = int(levels[i+1])

        if abs(number-next_number) < 4:
            if i == 0:
                if number < next_number: asc = True
                else: desc = True
            
            if asc and number >= next_number: break
            if desc and number <= next_number: break
                
            safe += 1
    return safe == len(levels)-1


with open('input.txt', 'r') as file:
    lines = file.readlines()

res = 0
safe_lines = []
for line in lines:
    if is_safe_line(line):
        res += 1
        safe_lines.append(line)

for line in lines:
    if line not in safe_lines:
        levels = line.replace("\n", "").split(" ")
        for i in range(len(levels)):
            modified_levels = levels[:i] + levels[i+1:]
            new_line = ""
            for modified_level in modified_levels:
                new_line = new_line + str(modified_level) + " "

            new_line = new_line[:len(new_line)-1]
            if is_safe_line(new_line):
                res += 1
                break

print("RESULT: " + str(res))