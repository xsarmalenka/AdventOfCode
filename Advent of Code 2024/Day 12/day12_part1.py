from collections import deque

def get_region_perimeter(region):
    region_perimeter = 4 * len(region)
    for (x, y) in region:
       
       # check south
       if (x+1, y) in region: region_perimeter -= 1
       
       # check north
       if (x-1, y) in region: region_perimeter -= 1
       
       # check west
       if (x, y-1) in region: region_perimeter -= 1
       
       # chesk east
       if (x, y+1) in region: region_perimeter -= 1

    return region_perimeter
    
def get_plant_positions(field, plant):
    positions = []
    for i, row in enumerate(field):
        for j, clm in enumerate(row):
            if clm == plant:
                positions.append((i, j))
    return positions

def get_plants(field):
    plants = []
    for i, row in enumerate(field):
        for j, clm in enumerate(row):
            if not clm in plants:
                plants.append(clm)
    return plants

def item_in_region(item, regions):
    check = False
    for region in regions:
        for position in region:
            if item == position:
                check = True
    return check

def get_regions(field, plant):
    plant_positions = get_plant_positions(field, plant)
    regions = []
    visited = set() 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

    def bfs(start): 
        queue = deque([start])
        region = set([start])
        visited.add(start)
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                neighbor = (x + dx, y + dy)
                if neighbor in plant_positions and neighbor not in visited:
                    visited.add(neighbor)
                    region.add(neighbor)
                    queue.append(neighbor)
        return region
    
    def position_in_any_region(position, regions):
        for region in regions:
            if position in region:
                return True, region
        return False, None

    for position in plant_positions:
        if position not in visited:  
            new_region = bfs(position)  
            regions.append(new_region)  

    return regions

def check(plant_positions, region):
    checksum = True
    for (x, y) in plant_positions:
        if not (x, y) in region:
            for (tx, ty) in region.copy():
                neigbour = 0

                # check south
                if tx+1 == x and ty == y: neigbour += 1

                # check north
                if tx-1 == x and ty == y: neigbour += 1

                # check west
                if tx == x and ty-1 == y: neigbour += 1

                # check east
                if tx == x and ty+1 == y: neigbour += 1

                if neigbour != 0:
                    checksum = False
                    region.add((x, y))
                    
    return region, checksum

file_name = 'input.txt'
#file_name = 'test_input3.txt'
#file_name = 'test_input2.txt'
#file_name = 'test_input.txt'

with open(file_name, 'r') as file:
    input = file.read()

field = input.split("\n")
plants = get_plants(field)
res = 0
for plant in plants:
    regions = get_regions(field, plant)
    i = 0
    for region in regions:
        perimeter = get_region_perimeter(region)
        res += len(region) * perimeter
        i += 1

print("\nRESULT: " + str(res))