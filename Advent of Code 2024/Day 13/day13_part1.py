from sympy import symbols, Eq, solve

def push(machine, x, y, button):
    machine_instrutions = machine.split("\n")
    for machine_instruction in machine_instrutions:
        if button in machine_instruction:
            instruction = machine_instruction
            break
    
    instructions = instruction.split(" ")
    x_move = int(instructions[2].split("+")[1].replace(",", ""))
    y_move = int(instructions[3].split("+")[1])
    return x + x_move, y + y_move

def get_move(machine, button):
    machine_instrutions = machine.split("\n")
    for machine_instruction in machine_instrutions:
        if button in machine_instruction:
            instruction = machine_instruction
            break
    
    instructions = instruction.split(" ")
    if button == "Prize":
        x = int(instructions[1].split("=")[1].replace(",", ""))
        y = int(instructions[2].split("=")[1])
    else:
        x = int(instructions[2].split("+")[1].replace(",", ""))
        y = int(instructions[3].split("+")[1])
    return x, y

def solver(machine):
    a_price = 3
    b_price = 1

    price = -1
    count_a = -1
    count_b = -1

    x_A, y_A = get_move(machine, "Button A")
    x_B, y_B = get_move(machine, "Button B")
    x_R, y_R = get_move(machine, "Prize")

    a, b = symbols('a b')
    eq1 = Eq(x_A * a + x_B * b, x_R)
    eq2 = Eq(y_A * a + y_B * b, y_R)
    solution = solve((eq1, eq2), (a, b))
    # print(f"Solver: x = {solution[a]}, y = {solution[b]}")

    if not "/" in str(solution[a]) and not "/" in str(solution[b]):
        price = a_price * solution[a] + b_price * solution[b]
        count_a = solution[a]
        count_b = solution[b]

    return price, count_a, count_b


def play(input):
    machines = input.split("\n\n")
    win_counter = 0
    price_sum = 0
    for machine in machines:
        price, a, b = solver(machine)
   
        if price != -1:
            win_counter += 1
            price_sum += price

    return price_sum

file_name = 'input.txt'
#file_name = 'test_input.txt'

with open(file_name, 'r') as file:
    input = file.read()

result = play(input)
print("\nRESULT: " + str(result))


