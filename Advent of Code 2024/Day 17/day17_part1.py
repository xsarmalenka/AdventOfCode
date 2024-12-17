def get_register_number(registers, label):
    registers_lines = registers.split("\n")
    for line in registers_lines:
        if label in line:
            return line.split(": ")[1]

def dv(operand, register):
    global register_A, register_B, register_C
    result = int(int(register_A) / 2**int(operand))

    if register == "A":
        register_A = result
    elif register == "B":
        register_B = result
    elif register == "C":
        register_C = result

def bxl(operand):
    global register_B
    register_B = int(register_B) ^ int(operand)
 
def bst(operand):
    global register_B
    register_B = int(operand) % 8

def bxc(operand):
    global register_B, register_C
    register_B = int(register_B) ^ int(register_C)

def out(operand):
    return int(operand) % 8

def jnz(operand):
    global register_A, instruction_pointer, pointer, program, change

    if int(register_A) != 0:
        instructions = program.split(": ")[1].split(",")
        pointer = int(operand)
        change = True
        instruction_pointer = 1

def run_instruction(instruction, operand, lit):
    global output
    int_instruction = int(instruction)

    if int_instruction == 0: dv(operand, "A")
    elif int_instruction == 1: bxl(lit)
    elif int_instruction == 2: bst(operand)
    elif int_instruction == 3: jnz(operand)
    elif int_instruction == 4: bxc(operand)
    elif int_instruction == 5:
        if output != "": output += ","
        output += str(out(operand)) 
    elif int_instruction == 6: dv(operand, "B")
    elif int_instruction == 7: dv(operand, "C")

def process():
    global register_A, register_B, register_C, output, instruction_pointer, pointer, program, change
    # program = "Program: 0,1,2,3"
    instructions = program.split(" ")[1].split(",")
    output = ""
    pointer = 0

    while pointer < len(instructions)-1:
        change = False
        instruction = instructions[pointer]
        operand = instructions[pointer+1]
        instruction_pointer = 2

        lit = operand
        if int(operand) == 4: operand = register_A
        elif int(operand) == 5: operand = register_B
        elif int(operand) == 6: operand = register_C

        run_instruction(instruction, operand, lit)
        if not change:
            pointer += instruction_pointer

    print(program)
    print("Register A: " + str(register_A))
    print("Register B: " + str(register_B))
    print("Register C: " + str(register_C))
    print("OUTPUT: " + output)

file_name = 'input.txt'
#file_name = 'test_input.txt'

with open(file_name, 'r') as file:
    input = file.read()

global register_A, register_B, register_C, output, instruction_pointer, pointer, program, change
registers, program = input.split("\n\n")

# test BST - OK
#registers = "Register A: 0\nRegister B: 0\nRegister C: 9"
#program = "Program: 2,6"

# test OUT - OK
#registers = "Register A: 10\nRegister B: 0\nRegister C: 0"
#program = "Program: 5,0,5,1,5,4"

# test ADV, OUT, JNZ - OK
#registers = "Register A: 2024\nRegister B: 0\nRegister C: 0"
#program = "Program: 0,1,5,4,3,0"

# test BXL - OK
#registers = "Register A: 0\nRegister B: 29\nRegister C: 0"
#program = "Program: 1,7"

# test BXC - OK
#registers = "Register A: 0\nRegister B: 2024\nRegister C: 43690"
#program = "Program: 4,0"

register_A = get_register_number(registers, "A")
register_B = get_register_number(registers, "B")
register_C = get_register_number(registers, "C")
change = False
process()