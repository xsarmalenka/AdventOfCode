from itertools import product

def second_search(left, numbers):
    operators = ["+", "*", "||"]
    all_combinations = product(operators, repeat=len(numbers)-1)

    for ops in all_combinations:
        result = numbers[0]
        for i, op in enumerate(ops):
            if op == "+":
                result += numbers[i+1]
            elif op == "*":
                result *= numbers[i+1]
            elif op == "||":
                result = int(str(result) + str(numbers[i+1]))
        if result == left: 
            return True
    return False


def evaluate_expression(left, numbers):
    operators = ["+", "*"]
    all_combinations = product(operators, repeat=len(numbers)-1)

    for ops in all_combinations:
        result = numbers[0]
        for i, op in enumerate(ops):
            if op == "+":
                result += numbers[i+1]
            elif op == "*":
                result *= numbers[i+1]
        if result == left:
            return True
    return False

def get_left_equation(equation):
    return int(equation.split(":")[0])

def get_right_equation(equation):
    number_list = []
    rights = equation.split(":")[1].split(" ")
    for right in rights:
        try:
            number_list.append(int(right))
        except: continue
    return number_list

def check_result(result, res):
    if result == res: return True
    else: return False

with open('test_input.txt', 'r') as file:
    equations = file.read().split("\n")

result = 0
for equation in equations:
    left_equation = get_left_equation(equation)
    right_equation = get_right_equation(equation)
    if evaluate_expression(left_equation, right_equation):
        result += left_equation
    else:
        if second_search(left_equation, right_equation):
            result += left_equation

print("\nRESULT: " + str(result))


