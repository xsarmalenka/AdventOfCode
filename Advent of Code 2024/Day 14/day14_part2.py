def pretty_print(map):
    print("\n")
    for row in map:
        print("".join(row))

def get_position(robot):
    position = robot.split(" ")[0]
    x = position.split(",")[0].replace("p=", "")
    y = position.split(",")[1]
    return int(y), int(x)

def get_speed(robot):
    speed = robot.split(" ")[1]
    x = speed.split(",")[0].replace("v=", "")
    y = speed.split(",")[1]
    return int(y), int(x) 

def visualization(input):
    global rows, cols
    robots = input.split("\n")
    positions = []
    speeds = []
    
    bathroom_visual = [["." for _ in range(cols)] for _ in range(rows)]

    for robot in robots:
        x, y = get_position(robot)
        positions.append((x, y))

        if bathroom_visual[x][y] != ".":
            count = int(bathroom_visual[x][y])
            number = str(count + 1)
        else:
            number = str(1)

        bathroom_visual[x][y] = number

        vx, vy = get_speed(robot)
        speeds.append((vx, vy))
    
    # pretty_print(bathroom_visual)
    return robots, positions, speeds

def matches_tree_pattern(grid, tree_pattern, start_row, start_col):
    pattern_height = len(tree_pattern)
    pattern_width = len(tree_pattern[0])
    
    if start_row + pattern_height > len(grid) or start_col + pattern_width > len(grid[0]):
        return False

    for i, pattern_row in enumerate(tree_pattern):
        grid_row = grid[start_row + i][start_col:start_col + pattern_width]
        if "".join(grid_row) != pattern_row:
            return False

    return True

def check_tree(positions):
    global tree_pattern, rows, cols

    pattern_height = len(tree_pattern)
    pattern_width = len(tree_pattern[0])

    for row in range(rows - pattern_height + 1):
        for col in range(cols - pattern_width + 1):
            if matches_tree_pattern(positions, tree_pattern, row, col):
                return True
    return False

def make_visual(positions):
    bathroom_visual = [["." for _ in range(cols)] for _ in range(rows)]
    for position in positions:
        x, y = position

        if bathroom_visual[x][y] != ".":
            count = int(bathroom_visual[x][y])
            number = str(count + 1)
        else:
            number = str(1)

        bathroom_visual[x][y] = number
    return bathroom_visual

def move(robots, positions, speeds):
    global rows, cols
    seconds = 0
    check = False

    while not check:
        for i, robot in enumerate(robots):
            new_robot_position_x = positions[i][0] + speeds[i][0]
            new_robot_position_y = positions[i][1] + speeds[i][1]
                
            if new_robot_position_x < 0: new_robot_position_x = rows + new_robot_position_x
            if new_robot_position_x > rows - 1: new_robot_position_x = new_robot_position_x - rows
            if new_robot_position_y < 0: new_robot_position_y = cols + new_robot_position_y
            if new_robot_position_y > cols - 1: new_robot_position_y = new_robot_position_y - cols

            positions[i] = (new_robot_position_x, new_robot_position_y)

        bathroom_visual = make_visual(positions)
        check = check_tree(bathroom_visual)
        print(str(seconds) + "-" + str(check))
        
        seconds += 1

    pretty_print(bathroom_visual)
    return seconds

file_name = 'input.txt'
#file_name = 'test_input.txt'

with open(file_name, 'r') as file:
    input = file.read()

global rows, cols, tree_pattern

if file_name == 'test_input.txt':
    rows = 7
    cols = 11
    tree_pattern = [
    "..1..",
    ".111."]
elif file_name == 'input.txt':
    rows = 103
    cols = 101
    tree_pattern = [
    "..1..",
    ".111.",
    "11111"]


robots, positions, speeds = visualization(input)
seconds = move(robots, positions, speeds)
print("\nRESULT: " + str(seconds))