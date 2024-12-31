def get_computer_list(connections):
    computers = []
    for connection in connections:
        for connect in connection.split("-"):
            if not connect in computers:
                computers.append(connect)

    return sorted(computers)

def get_computers(connections, computer):
    computers = []
    for connection in connections:
        for connect in connection.split("-"):
            if not connect in computers and computer in connection and not connect == computer:
                computers.append(connect)

    return sorted(computers)

def check_result(item, results):
    for result in results:
        if result.startswith(item):
            return False
    return True

def find_sets(connections, computers, number):
    results = set()

    computer_list = set()
    for computer in computers:
        computer_list.add(computer)
    computer_list = sorted(computer_list)
    
    for computer in computer_list:
        computer_connections = get_computers(connections, computer)
        len_computer_connections = len(computer_connections)
        part = [computer, 0, 0]
        for computer_connection in computer_connections:
            if check_result(computer_connection, results):
                part[1] = computer_connection
                next_computer_connections = get_computers(connections, part[1])
                common_items = set(computer_connections) & set(next_computer_connections)

                for common_item in common_items:
                    if check_result(common_item, results):
                        part[2] = common_item
                        part_line = part[0] + "," + part[1] + "," + part[2]
                        duplicity_part_line = part[0] + "," + part[2] + "," + part[1]
                        if not duplicity_part_line in results:
                            results.add(part_line)
    return sorted(results)
    
def find_historic_sets(parts, char):
    results = []

    for part in parts:
        sub_parts = part.split(",")
        for sub_part in sub_parts:
            if sub_part.startswith(char) and not part in results:
                results.append(part)

    return results

file_name = 'input.txt'
#file_name = 'test_input.txt'

with open(file_name, 'r') as file:
    input = file.read()

connections = input.split("\n")
computers = get_computer_list(connections)
sets_3 = find_sets(connections, computers, 3)
historic_sets = find_historic_sets(sets_3, "t")

print("\nRESULT: " + str(len(historic_sets)))