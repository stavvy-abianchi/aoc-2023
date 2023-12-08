from modules.input import read_input

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
    
    node = 'AAA'
    step_count = 0
    while node != 'ZZZ':
        for dir in directions:
            dir = 0 if dir == 'L' else 1
            step_count += 1
            node = node_map[node][dir]
    
    print(step_count)

        