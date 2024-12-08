with open('input.txt', 'r') as file:
    lines = file.readlines()

res = 0
for line in lines:
    levels = []
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
            if i == len(levels)-2 and safe == len(levels)-1:
                res += 1

print("RESULT: " + str(res))