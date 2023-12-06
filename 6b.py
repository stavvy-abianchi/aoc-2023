from modules.input import read_input
import math

if __name__ == "__main__":
    game_data = read_input(__file__)

    times = []
    record_dist = []
    for row in range(0, len(game_data)):
        if row == 0:
            times = [time for time in game_data[row].split(":")[1].split(" ") if time != ""]
        if row == 1:
            record_dist = [dist for dist in game_data[row].split(":")[1].split(" ") if dist != ""]
    
    ways_to_win = []
    for race in range(0, len(times)):
        print(f"Starting new race: {times[race]} -> record: {record_dist[race]}")
        wins = []

        # ms represents the amount of time to hold the button down
        for ms in range(0, int(times[race]) + 1):
            speed = ms
            race_length = int(times[race])
            distance = (race_length - speed) * speed

            if distance > int(record_dist[race]):
                wins.append(distance)
        
        #print(wins)
        ways_to_win.append(len(wins))
    
    print(math.prod(ways_to_win))