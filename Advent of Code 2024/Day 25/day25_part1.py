def get_pin_heights(keys):
    key_heights = []
    key_pins = []
    for key in keys:
        help_pin_heights = []
        key_lines = key.split("\n")
        for i, key_row in enumerate(key_lines):
            for j, key_column in enumerate(key_row):
                if key_column == ".":
                    test = len(key_lines)-2
                    help_pin_heights.append((i, j))

        key_height = []
        key_pin = []
        for i in range(test):
            j = 0
            for help_pin_height in help_pin_heights:
                (x, y) = help_pin_height
                if i == y:
                    j += 1

            if "." in key[0]: key_height.append(len(key_lines)-j-1)
            else: key_pin.append(len(key_lines)-j-1)

        if "." in key[0]: key_heights.append(key_height)
        else: key_pins.append(key_pin)
        
    print("\nKEY PINS: ")
    for key_pin in key_pins:
        print(key_pin)

    print("\nKEY HEIGHTS: ")
    for key_height in key_heights:
        print(key_height)
    
    return key_pins, key_heights

def find_result(pins, keys):
    result = 0
    for pin in pins:
        for key in keys:
            print("\nPIN: " + str(pin) + " + KEY: " + str(key))
            check_pin = 0
            for i in range(len(pin)):
                if int(pin[i]) + int(key[i]) <= len(pin):
                    check_pin += 1

            if check_pin == len(pin):
                result += 1
    return result

file_name = 'input.txt'
#file_name = 'test_input.txt'

with open(file_name, 'r') as file:
    input = file.read()

keys = input.split("\n\n")
pins, keys = get_pin_heights(keys)
result = find_result(pins, keys)
print("\nRESULT: " + str(result))