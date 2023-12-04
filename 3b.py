from modules.input import read_input

gear_parts = {}

def add_part_num(cell_id, gear_cell):
    val = num_map.get(cell_id)
    if val is not None:
        part_nums.append(int(val))
        gear_parts[gear_cell].append(val)
        return True
    else:
        return False

def check_neighbors(cell_idx):
    x, y = get_cell_x_y(cell_idx)
    gear_parts[cell_idx] = []
    #print(f'checking neighbors for x:{x} y:{y}')
    neighbor_count = 0
    if y > 0:
        # check up
        if not add_part_num(get_cell_idx(x, y - 1), cell_idx):
        # check up left
            if x > 0:
                if add_part_num(get_cell_idx(x - 1, y - 1), cell_idx):
                    neighbor_count += 1
        # check up right
            if x < width - 1:
                if add_part_num(get_cell_idx(x + 1, y - 1), cell_idx):
                    neighbor_count += 1
        else:
            neighbor_count += 1

    if y < height - 1:
        # check down
        if not add_part_num(get_cell_idx(x, y + 1), cell_idx):

        # check down left
            if x > 0:
                if add_part_num(get_cell_idx(x - 1, y + 1), cell_idx):
                    neighbor_count += 1

        # check down right
            if x < width - 1:
                if add_part_num(get_cell_idx(x + 1, y + 1), cell_idx):
                    neighbor_count += 1
        else:
            neighbor_count += 1
    
    # check left
    if x > 0:
        if add_part_num(get_cell_idx(x - 1, y), cell_idx):
            neighbor_count += 1

    # check right
    if x < width - 1:
        if add_part_num(get_cell_idx(x + 1, y), cell_idx):
            neighbor_count += 1
    
    if neighbor_count == 2:
        print(gear_parts[cell_idx])
        gear_parts[cell_idx] = int(gear_parts[cell_idx][0]) * int(gear_parts[cell_idx][1])
    else:
        gear_parts.pop(cell_idx)

# y * width + x
def get_cell_idx(x, y):
    # print(f'x: {x} y: {y} idx: {y * width + x}')
    return y * width + x

def get_cell_x_y(cell_idx):
    return cell_idx % width,  int(cell_idx / width)

if __name__ == "__main__":
    game_data = read_input(__file__)

    width = len(game_data[0])
    height = len(game_data)
    print(f'Loaded map with -> Rows: {height} Columns: {width} for a total size of {height * width}')

    part_map = [None] * width * height

    part_ids = []
    found_nums = []
    num_map = {}
    part_nums = []

    for row_idx in range(0, height):
        found_num = None
        for col_idx in range(0, width):
            cell_idx = row_idx * width + col_idx # y * width + x
            # print(f'x:{col_idx} y:{row_idx} -> {cell_idx}')
            part_map[cell_idx] = game_data[row_idx][col_idx]
            cell_val = part_map[cell_idx]

            if cell_val != '.' and not cell_val.isdigit():
                if cell_val == '*':
                    part_ids.append(cell_idx)
            
            if cell_val == '.':
                part_map[cell_idx] = " "
            
            if cell_val.isdigit():
                if found_num is None:
                    found_num = f'{cell_val}'
                else:
                    found_num += cell_val
            else:
                if found_num is not None:
                    found_nums.append(found_num)
                    for cell in range((cell_idx - (len(found_num) - 1) - 1), cell_idx):
                        num_map[cell] = found_num
                    found_num = None
            
            if col_idx == width - 1 and found_num is not None: # end of row so a number can't extend past this point so finish a number
                found_nums.append(found_num)
                for cell in range((cell_idx - (len(found_num) - 1)), cell_idx + 1):
                    num_map[cell] = found_num
                #print(f'end of row {found_num}:{cell_idx}')
                found_num = None

    for part in part_ids:
        check_neighbors(part)

    print(sum(gear_parts.values()))