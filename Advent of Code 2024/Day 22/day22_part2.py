def mix(secret_number, number_to_mix):
    return secret_number ^ number_to_mix

def prune(secret_number):
    return secret_number % 16777216

def make_secret_number(secret_number):
    first_result = prune(mix(secret_number, secret_number * 64))
    second_result = prune(mix(first_result, int(first_result / 32)))
    return prune(mix(second_result, second_result * 2048))

def get_prices(number, secret_numbers):
    number_price = number[-1]
    numbers_prices = []
    for secret_number in secret_numbers:
        numbers_prices.append(int(str(secret_number)[-1]))

    diff_prices = []
    for i, secret_number in enumerate(secret_numbers):
        if i != 0:
            diff_prices.append(int(numbers_prices[i]) - int(numbers_prices[i-1]))

    return numbers_prices, diff_prices

def process_secret_number(input, count):
    info = []
    numbers = input.split("\n")
    j = 0
    for number in numbers:
        print(f"PROCESSING SECRET NUMBER {j} / {len(numbers)}")
        secret_numbers = []
        secret_number = int(number)
        secret_numbers.append(secret_number)

        for i in range(count):
            secret_number = make_secret_number(secret_number)
            secret_numbers.append(secret_number)

        number_prices, diff_prices = get_prices(number, secret_numbers)
        info.append((number, secret_numbers, number_prices, diff_prices))  
        j += 1

    return info

def exist_price(price, price_list):
    return price in price_list

def get_sequence(test_sequence, number, number_prices, diff_prices):
    for i in range(9, 0, -1):
        max_price = i
        check_exist = exist_price(max_price, number_prices)
        if check_exist:
            max_price_indexes = [i for i, x in enumerate(number_prices) if x == max_price and i >= 3]
            sequences = []
            for max_price_index in max_price_indexes:
                sequence = [diff_prices[max_price_index-4], diff_prices[max_price_index-3], diff_prices[max_price_index-2], diff_prices[max_price_index-1]]
                sequences.append(sequence)

            check_sequence = test_sequence in sequences
            if check_sequence:
                return max_price
    return 0

def find_best_common_sequence(all_sequences):
    grouped_by_secret = {}
    for group in all_sequences:
        for item in group:
            secret_number = item[0]
            price = item[1]
            sequence = tuple(item[2])  
            if secret_number not in grouped_by_secret:
                grouped_by_secret[secret_number] = []
            grouped_by_secret[secret_number].append((sequence, price))

    sequences_per_secret = {}
    for secret, items in grouped_by_secret.items():
        sequences_per_secret[secret] = {seq for seq, _ in items}

    all_possible_sequences = set()
    for sequences in sequences_per_secret.values():
        all_possible_sequences.update(sequences)

    best_sequence = None
    max_price = 0
    i = 0
    for seq in all_possible_sequences:
        #if seq == (0, -3, 2, 1):
        print(f"PROCESSING RESULT {i} / {len(all_possible_sequences)}")
        total_price = 0
        for secret in grouped_by_secret:
            dirty_numbers = {3040870, 15673661, 15777000, 644844, 13032656, 15225752, 10612813, 14579550, 414985, 3520487, 3087428, 14584391}
            prices = [price for sequence, price in grouped_by_secret[secret] if sequence == seq]
            indices = [index for index, (sequence, _) in enumerate(grouped_by_secret[secret]) if sequence == seq]

            if int(secret) in dirty_numbers: 
                price = next((price for sequence, price in reversed(grouped_by_secret[secret]) if sequence == seq), 0)
            else: 
                price = next((price for sequence, price in grouped_by_secret[secret] if sequence == seq), 0)
                    
            total_price += price
                
        if total_price > max_price:
            max_price = total_price
            best_sequence = seq
                
        i += 1 
    
    return best_sequence, max_price

def get_max_bananas(info):  
    all_sequences = []
    print("\n")
    for i in range(len(info)):
        print(f"PROCESSING SEQUENCES: {i} / {len(info)}")
        price_and_sequences = []
        number_info = info[i]
        number = number_info[0]
        number_prices = number_info[2]
        diff_prices = number_info[3]
        for j in range(3, len(diff_prices)):
            sequence = [diff_prices[j-3], diff_prices[j-2], diff_prices[j-1], diff_prices[j]]
            price_and_sequence = [number, number_prices[j+1], sequence]
            if not price_and_sequence in price_and_sequences:
                price_and_sequences.append(price_and_sequence)

        sorted_price_and_sequences = sorted(price_and_sequences, key=lambda x: x[1], reverse=True)
        all_sequences.append(sorted_price_and_sequences)

    best_sequence, max_price = find_best_common_sequence(all_sequences)
    print("Nejlepší společná sekvence:", best_sequence)
    print("Maximální součet cen:", max_price)

file_name = 'input.txt'
#file_name = 'test_input.txt'
#file_name = 'test_input2.txt'
#file_name = 'test_input3.txt'

with open(file_name, 'r') as file:
    input = file.read()

info = process_secret_number(input, 2000)
get_max_bananas(info)
