from modules.input import read_input

def check_val(map_val_range_offset, val):
    for map_val in map_val_range_offset:
        if val in map_val[0]:
            return val - map_val[1]
    
    return val

if __name__ == "__main__":
    game_data = read_input(__file__)

    seeds = []
    map_of_maps = {}
    map_name = None
    map_list = []
    for data_row_idx in range(0, len(game_data)):
        data_row = game_data[data_row_idx]

        if data_row_idx == 0:
            seeds = data_row.split(":")[1].strip().split(" ")
        else:
            if data_row == '':
                print("no data - reset map_name")
                map_name = None
            elif "map" in data_row:
                map_name = data_row.split(" ")[0]
                map_of_maps[map_name] = []
                map_list.append(map_name)
                print(f"found new map -> {map_name}")
            else: #populating data
                print(f'add to {map_name} -> {data_row}')
                #destination start, source start, range length
                dest_start, source_start, length = map(int, data_row.split(" "))
                cur_map = map_of_maps[map_name]
                cur_map.append([range(source_start, source_start + length), source_start - dest_start]) # source range, dest offset
    locations = []
    for seed in seeds:
        soil = check_val(map_of_maps['seed-to-soil'], int(seed)) 
        fertilizer = check_val(map_of_maps['soil-to-fertilizer'], soil) 
        water = check_val(map_of_maps['fertilizer-to-water'], fertilizer) 
        light = check_val(map_of_maps['water-to-light'], water) 
        temperature = check_val(map_of_maps['light-to-temperature'], light)
        humidity = check_val(map_of_maps['temperature-to-humidity'], temperature)
        location = check_val(map_of_maps['humidity-to-location'], humidity)
        locations.append(location)
    
    print(min(locations))
        