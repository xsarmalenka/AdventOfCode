from itertools import product

def evaluate_expression(left, numbers):
    from itertools import product
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

def find_operators(left, right):
    operators = ["+", "*"]
    operators_list = []
    help_list = []
    new_help_list = []

    for i in range(len(right)-1):
        first_number = right[i]
        second_number = right[i+1]
        for operator in operators:
            if len(right) == 2:
                if i == 0:
                    if operator == "+": res = first_number + second_number
                    elif operator == "*": res = first_number * second_number

                result = check_result(left, res)
                if result: operators_list.append(operator)
            elif len(right) > 2:
                if i == 0: # first number
                    if operator == "+":
                        res = first_number + second_number
                        help_list.append([res, [operator]])
                    elif operator == "*":
                        res = first_number * second_number
                        help_list.append([res, [operator]])
            
                elif i == len(right)-2: # last number
                    for help_line in help_list:
                        help = help_line[0]
                        if operator == "+": res = help + second_number
                        elif operator == "*": res = help * second_number

                        result = check_result(left, res)
                        if result: 
                            help_line[1].append(operator)
                            operators_list.append(help_line[1])
                else:
                    new_help_list = []
                    for help_line in help_list:
                        help = help_line[0]
                        if operator == "+": res = help + second_number
                        elif operator == "*": res = help * second_number
                        
                        new_list = help_line[1] + [operator]
                        new_help_list.append([res, new_list])

        if len(new_help_list) > 0:
            help_list = new_help_list
    return operators_list

with open('input.txt', 'r') as file:
    equations = file.read().split("\n")

print(equations)
result = 0
for equation in equations:
    left_equation = get_left_equation(equation)
    right_equation = get_right_equation(equation)
    if evaluate_expression(left_equation, right_equation):
        result += left_equation

print("\nRESULT: " + str(result))


