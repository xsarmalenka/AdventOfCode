from itertools import permutations

def find_uncorrect_updates(updates, rules):
    uncorrect_updates = []
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

        if correct != numbers_count-1:
            uncorrect_updates.append(update)

    return uncorrect_updates

def get_middle_number(update):
    numbers = update.split(",")
    numbers_count = len(numbers)
    return int(numbers[numbers_count // 2])

def make_correct(uncorrect_updates, rules):
    correct_updates = []
    for update in uncorrect_updates:
        update_numbers = update.split(",")
        correct_update = []
        for i in range(len(update_numbers)):
            correct_update.append('')

        for update_number in update_numbers:
            correct = 0
            skip = 0
            for number in update_numbers:
                if update_number != number and number != correct_update:
                    for rule in rules:
                        if update_number in rule and number in rule:
                            left_rule = rule.split("|")[0]
                            right_rule = rule.split("|")[1]

                            update_number_position = update_numbers.index(update_number)
                            number_position = update_numbers.index(number)

                            if update_number == left_rule and number == right_rule:
                                if update_number_position < number_position: correct += 1
                                else: skip -= 1
                            elif update_number == right_rule and number == left_rule:
                                if update_number_position > number_position: correct += 1
                                else: skip += 1
            if skip != 0: correct_update[update_number_position+skip] = update_number
            else: correct_update[update_number_position] = update_number

            if correct == len(update_numbers)-1: correct_update[update_number_position] = update_number

        correct_updates.append(",".join(correct_update))
    return correct_updates

# Main program
with open('input.txt', 'r') as file:
    input = file.read()

rules = [line for line in input.split("\n") if "|" in line]
updates = [line for line in input.split("\n") if "," in line]
uncorrect_updates = find_uncorrect_updates(updates, rules)
correct_updates = make_correct(uncorrect_updates, rules)

result = 0
for update in correct_updates:
    middle_number = get_middle_number(update)
    result += middle_number

print("\nRESULT: " + str(result))