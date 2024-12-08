def find_correct_updates(updates, rules):
    correct_updates = []
    for update in updates:
        numbers = update.split(",")
        numbers_count = len(numbers)
        correct = 0
        for i in range(1, numbers_count):
            current_number = numbers[i]
            prev_number = numbers[i-1]
            for rule in rules:
                if current_number in rule and prev_number in rule:
                    left_rule_num = rule.split("|")[0]
                    right_rule_num = rule.split("|")[1]
                    if left_rule_num == prev_number and right_rule_num == current_number:
                        correct += 1

        if correct == numbers_count-1:
            correct_updates.append(update)

    return correct_updates

def get_middle_number(update):
    numbers = update.split(",")
    numbers_count = len(numbers)
    return int(numbers[numbers_count // 2])

# Main program
with open('input.txt', 'r') as file:
    input = file.read()

rules = [line for line in input.split("\n") if "|" in line]
updates = [line for line in input.split("\n") if "," in line]
correct_updates = find_correct_updates(updates, rules)

result = 0
for update in correct_updates:
    middle_number = get_middle_number(update)
    result += middle_number

print("\nRESULT: " + str(result))