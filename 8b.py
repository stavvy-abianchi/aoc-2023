from modules.input import read_input
import copy
import math
if __name__ == "__main__":
    game_data = read_input(__file__)

    directions = ''
    node_map = {}
    for row in range(0, len(game_data)):
        if row == 0:
            directions = game_data[row].strip()
        else:
            row = game_data[row]

            if len(row) > 1:
                node, options = row.split(" = ")
                options = options.strip("()").split(", ")
                
                node_map[node] = options

    nodes = {k: v for k,v in node_map.items() if k[2] == 'A'}.keys()

    step_count = 0
    nodes = ([node for node in nodes if node[2] != 'Z'])

    cycle_map = {}
    # solve for each node
    for node in nodes:
        step_count = 0
        temp = copy.deepcopy(node)
        while temp[2] != 'Z':
            for dir in directions:
                step_count += 1
                dir = 0 if dir == 'L' else 1
            
                temp = node_map[temp][dir]
        
        cycle_map[node] = step_count

    print(math.lcm(*cycle_map.values()))
        