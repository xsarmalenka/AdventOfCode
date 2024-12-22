def mix(secret_number, number_to_mix):
    return secret_number ^ number_to_mix

def prune(secret_number):
    return secret_number % 16777216

def make_secret_number(secret_number):
    first_result = prune(mix(secret_number, secret_number * 64))
    second_result = prune(mix(first_result, int(first_result / 32)))
    return prune(mix(second_result, second_result * 2048))

def process(input):
    sum = 0
    numbers = input.split("\n")
    for number in numbers:
        secret_number = int(number)
        for i in range(2000):
            secret_number = make_secret_number(secret_number)
        print(str(number) + ": " + str(secret_number))
        sum += secret_number
    return sum

file_name = 'input.txt'
#file_name = 'test_input.txt'
#file_name = 'test_input2.txt'

with open(file_name, 'r') as file:
    input = file.read()

result = process(input)
print("\nRESULT: " + str(result))