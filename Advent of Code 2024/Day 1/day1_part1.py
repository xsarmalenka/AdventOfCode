with open('input.txt', 'r') as file:
    lines = file.readlines()

left_column = []
right_column = []

for line in lines:
    numbers = list(map(int, line.split()))
    left_column.append(numbers[0])
    right_column.append(numbers[1])

left_column.sort()
right_column.sort()

res = 0
if len(left_column) == len(right_column):
    for i in range(len(left_column)):
        res = res + abs(left_column[i] - right_column[i])

print(str(res))