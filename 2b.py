from modules.input import read_input

def convert_game_data(game_results):
    cube_counts = { "green": 0, "blue": 0, "red": 0}
    for game_result in game_results.split(';'):
        for cube_stats in game_result.split(','):
            cube_count, cube_color = cube_stats.strip().split(' ')
            cube_counts[cube_color] = int(cube_count) if int(cube_count) > cube_counts[cube_color] else cube_counts[cube_color]
    return(cube_counts)

if __name__ == "__main__":
    game_data = read_input(__file__)

    game_results = []
    game_sum = 0
    for game in game_data:
        game_number, game_results = game.split(':')
        game_number = game_number.split(' ')[1] # get just the number
        results = convert_game_data(game_results)
        power = results["blue"] * results["green"] * results["red"]
        game_sum += power

    print(game_sum)