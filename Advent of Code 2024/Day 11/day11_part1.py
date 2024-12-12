def get_even(number):
    even = False
    numbers = list(number)
    res = len(numbers) % 2

    if res == 0:
        even = True

    return even

def blink(input, blink):
    stones = input.split(" ")
    test_stones = stones

    for i in range(blink):
        blink_stones = []

        print("\nBLINK: " + str(i+1) + "/" + str(blink))
        for j, stone in enumerate(test_stones):

            if int(stone) == 0:
                blink_stones.append(str(1))
            elif get_even(stone):
                numbers = list(stone)
                middle = len(numbers) // 2

                first_number = ""
                for k in range(0, middle):
                    first_number += numbers[k]

                second_number = ""
                zero = 0
                for k in range(middle, len(numbers)):
                    if numbers[k] == str(0):
                        zero += 1
                    second_number += numbers[k]

                if zero != 0:
                    zero_test = 0
                    for k in range(middle, len(numbers)):
                        if numbers[k] == str(0):
                            zero_test += 1
                        else: 
                            second_number = second_number[zero_test:]
                            break 
                blink_stones.append(str(first_number))
                blink_stones.append(str(second_number))

            else:
                blink_stones.append(str(int(stone) * 2024))

        #print("*** AFTER " + str(i+1) + " blink:\n" + " ".join(map(str, blink_stones)))
        test_stones = blink_stones
    return blink_stones

#file_name = 'test_input2.txt'    
#file_name = 'test_input.txt'
file_name = 'input.txt'

with open(file_name, 'r') as file:
    input = file.read()

print("\nINPUT: " + input)

stones = blink(input, 25)
print("\nRESULT: " + str(len(stones)))



