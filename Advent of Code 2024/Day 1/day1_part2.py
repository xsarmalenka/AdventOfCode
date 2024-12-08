with open('input.txt', 'r') as file:
    lines = file.readlines()

left_column = []
right_column = []

for line in lines:
    numbers = list(map(int, line.split()))
    left_column.append(numbers[0])
    right_column.append(numbers[1])

res = 0
for left_number in left_column:
    counter = 0
    for right_number in right_column:
        if left_number == right_number:
            counter += 1
    res = res + (counter * left_number)

print(str(res))