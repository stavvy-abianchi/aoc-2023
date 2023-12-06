from modules.input import read_input
import threading
import os

from threading import Thread

def check_val(map_val_range_offset, val):
    #print(map_val_range_offset)
    for map_val in map_val_range_offset:
        map_range = map_val[0]
        start = map_range[0]
        end = map_range[1]
        if start <= val <= end:
            #print(val - map_val[1], val, map_val[1])
            return val - map_val[1]
    #print(f'{val} ----')
    return val

def burn_cpu(seed_data, storage, index):
    #print(seed_data, storage, index)
    min_loc = 100000000000000000
    for true_seed in range(seed_data[0], seed_data[0] + seed_data[1]):
        if true_seed % 1000000 == 0:
            print(f'doing gods work from index: {index}')
            #print(f"another bottle of beer {true_seed} / {seed[0] + seed[1]}")
        soil = check_val(map_of_maps['seed-to-soil'], int(true_seed)) 
        fertilizer = check_val(map_of_maps['soil-to-fertilizer'], soil) 
        water = check_val(map_of_maps['fertilizer-to-water'], fertilizer) 
        light = check_val(map_of_maps['water-to-light'], water) 
        temperature = check_val(map_of_maps['light-to-temperature'], light)
        humidity = check_val(map_of_maps['temperature-to-humidity'], temperature)
        location = check_val(map_of_maps['humidity-to-location'], humidity)
        if location < min_loc:
            min_loc = location
            storage[index] = min_loc

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
                cur_map.append([[source_start, source_start + length], source_start - dest_start]) # source range, dest offset
    locations = []
    min_location = 10000000000000000
    #print(len(seeds))

    threads = [None] * len(seeds)
    results = [None] * len(seeds)
    #print(seeds)
    for i in range(len(threads)):
        threads[i] = Thread(target=burn_cpu, args=(seeds[i], results, i))
        threads[i].start()

    for i in range(len(threads)):
        threads[i].join()
    
    print(min(results))
    quit()
    for seed in range(0, len(seeds)):
        seed = seeds[seed]
        for true_seed in range(seed[0], seed[0] + seed[1]):
            if true_seed % 1000000 == 0:
                print(f"another bottle of beer {true_seed} / {seed[0] + seed[1]}")
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
    
    print(min(locations))
        