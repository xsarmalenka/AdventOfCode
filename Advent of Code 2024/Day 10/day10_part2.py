def get_positions(input, target):
    positions = set()
    map = input.split("\n")
    for i, row in enumerate(map):
        for j, clm in enumerate(row):
            if clm == str(target):
                positions.add((i, j))
    return positions

def go_trail(input, head, trailtail_position):
    global trailtail
    trail = False
    map = [list(line) for line in input.split("\n")]
    result = 0

    current_position = head
    head_char = map[head[0]][head[1]]

    def explore(position, next_number, result, trailtail_position):

        if next_number == trailtail+1: 
            return result 

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        candidates = []

        for direct in directions:
            nx, ny = position[0] + direct[0], position[1] + direct[1]

            if 0 <= nx < len(map) and 0 <= ny < len(map[0]):
                if map[nx][ny] == str(next_number):
                    candidates.append((nx, ny))

                    if (nx,ny) == trailtail_position:
                        result += 1

        if len(candidates) == 0:
            return result
        elif len(candidates) == 1:
            return explore(candidates[0], next_number + 1, result, trailtail_position)
        else:
            for candidate in candidates:
                result = explore(candidate, next_number + 1, result, trailtail_position) 
        return result

    vysledek = explore(current_position, int(head_char) + 1, result, trailtail_position)
    return vysledek

def get_score(input):
    
    result = 0
    trailhead_positions = get_positions(input, trailhead)
    trailtail_positions = get_positions(input, trailtail)
    for trailhead_position in trailhead_positions:
        for trailtail_position in trailtail_positions:
            res = go_trail(input, trailhead_position, trailtail_position)
            result += res

    return result

#file_name = 'test_input4.txt'
#file_name = 'test_input6.txt'
#file_name = 'test_input5.txt'
#file_name = 'test_input2.txt'
file_name = 'input.txt'

with open(file_name, 'r') as file:
    input = file.read()

global trailtail
global trailhead
trailtail = 9
trailhead = 0

result = get_score(input)
print("\nRESULT: " + str(result))


