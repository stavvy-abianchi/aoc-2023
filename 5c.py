from modules.input import read_input

def check_val(map_val_range_offset, val):
    for map_val in map_val_range_offset:
        map_range = map_val[0]
        start = map_range[0]
        end = map_range[1]
        if start <= val <= end:
            #print(val - map_val[1], val, map_val[1])
            return val - map_val[1]
    #print(f'{val} ----')
    return val

def get_valid_range():
    pass

if __name__ == "__main__":
    game_data = read_input(__file__)

    seeds = []
    map_of_maps = {}
    map_name = None
    map_list = []
    for data_row_idx in range(0, len(game_data)):
        data_row = game_data[data_row_idx]

        if data_row_idx == 0:
            raw_seeds = data_row.split(":")[1].strip().split(" ")
            for idx in range(0, len(raw_seeds), 2):
                seeds.append([int(raw_seeds[idx]), int(raw_seeds[idx + 1])])
        else:
            if data_row == '':
                map_name = None
            elif "map" in data_row:
                map_name = data_row.split(" ")[0]
                map_of_maps[map_name] = []
                map_list.append(map_name)
            else: #populating data
                dest_start, source_start, length = map(int, data_row.split(" "))
                cur_map = map_of_maps[map_name]
                print(f'{map_name} -> doing shit')
                #for key in range(source_start, source_start + length):
                #    cur_map[key] = key - (source_start - dest_start)
                cur_map.append([[source_start, source_start + length], source_start - dest_start]) # source range, dest offset
    locations = []

    #print(seeds)
    min_location = 1000000000000
    #print(map_of_maps['humidity-to-location'])
    
    loc_count=0
    #for row in map_of_maps['humidity-to-location']:
    #    for val in range(row[0][0], row[0][1]):
    #        locations.append(val - row[1])
    #        loc_count += 1
    #        if loc_count % 10000 == 0:
    #            print(loc_count)
    #for
    #already_calc = {}
    #for location_range in map_of_maps['humidity-to-location']:
    #    pass
    #    print(location_range)
    for seed in range(0, len(seeds)):
        print(f'{seed} / {len(seeds) - 1}')
        seed = seeds[seed]
        for true_seed in range(seed[0], seed[0] + seed[1]):
    #        #if true_seed not in already_calc:
    #            #already_calc[true_seed] = None
    #        if true_seed % 1000000 == 0:
    #                #print(len(already_calc))
                #print(true_seed, seed[0], seed[1])
         #       print(f"another bottle of beer {true_seed} / {seed[0] + seed[1]}")
            soil = check_val(map_of_maps['seed-to-soil'], int(true_seed)) 
            fertilizer = check_val(map_of_maps['soil-to-fertilizer'], soil) 
            water = check_val(map_of_maps['fertilizer-to-water'], fertilizer) 
            light = check_val(map_of_maps['water-to-light'], water) 
            temperature = check_val(map_of_maps['light-to-temperature'], light)
            humidity = check_val(map_of_maps['temperature-to-humidity'], temperature)
            location = check_val(map_of_maps['humidity-to-location'], humidity)
            if location < min_location:
                min_location = location
                print("found new best location")
    #print(map_of_maps['humidity-to-location'])
    #print(loc_count)
    print(min_location)
    #print(already_calc) 