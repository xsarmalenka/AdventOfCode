def pretty_print(map):
    print("\n")
    for row in map:
        print(row)

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

def move(robots, positions, speeds, seconds):
    global rows, cols
    for i, robot in enumerate(robots):
        robot_speed = speeds[i]
        for m in range(seconds): # move
            new_robot_position_x = positions[i][0] + speeds[i][0]
            new_robot_position_y = positions[i][1] + speeds[i][1]
                
            if new_robot_position_x < 0: 
                new_robot_position_x = rows + new_robot_position_x

            if new_robot_position_x > rows - 1: 
                new_robot_position_x = new_robot_position_x - rows

            if new_robot_position_y < 0: 
                new_robot_position_y = cols + new_robot_position_y

            if new_robot_position_y > cols - 1: 
                new_robot_position_y = new_robot_position_y - cols

            positions[i] = (new_robot_position_x, new_robot_position_y)

    bathroom_visual = [["." for _ in range(cols)] for _ in range(rows)]
    for position in positions:
        x, y = position

        if bathroom_visual[x][y] != ".":
            count = int(bathroom_visual[x][y])
            number = str(count + 1)
        else:
            number = str(1)

        bathroom_visual[x][y] = number
    #pretty_print(bathroom_visual)
    return bathroom_visual

def get_safety_quadrant(positions, quadrant):
    global rows, cols
    safety = 0

    if quadrant == 1:
        start_row = 0
        start_clm = 0
        end_row = rows // 2 - 1
        end_clm = cols // 2 - 1 
    elif quadrant == 2:
        start_row = 0
        start_clm = cols // 2 + 1
        end_row = rows // 2 - 1
        end_clm = cols - 1
    elif quadrant == 3:
        start_row = rows // 2 + 1
        start_clm = 0
        end_row = rows - 1
        end_clm = cols // 2  - 1
    elif quadrant == 4:
        start_row = rows // 2 + 1
        start_clm = cols // 2 + 1
        end_row = rows - 1
        end_clm = cols - 1

    for i in range(start_row, end_row+1):
        for j in range(start_clm, end_clm+1):
            if positions[i][j] != ".":
                safety += int(positions[i][j])

    return safety

def get_safety(positions):
    quadrants = []

    for i in range(1, 5):
        quadrant = get_safety_quadrant(positions, i)
        print("QUADRANT res: " + str(quadrant))
        quadrants.append(quadrant)
    
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

file_name = 'input.txt'
#file_name = 'test_input.txt'

with open(file_name, 'r') as file:
    input = file.read()

global rows
global cols

# test_input
seconds = 100
if file_name == 'test_input.txt':
    rows = 7
    cols = 11
elif file_name == 'input.txt':
    rows = 103
    cols = 101

robots, positions, speeds = visualization(input)
positions = move(robots, positions, speeds, seconds)
result = get_safety(positions)
print("\nRESULT: " + str(result))


