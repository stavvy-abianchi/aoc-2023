from modules.input import read_input
import re

if __name__ == "__main__":
    input = read_input(__file__)

    calibration_values = []

    for cal_row in input:
        first_digit = 0
        last_digit = 0

        for char in range(0, len(cal_row)):
            if (cal_row[char].isdigit()):
                first_digit = cal_row[char]
                break

        for char in range(len(cal_row) -1, -1, -1):
            if (cal_row[char].isdigit()):
                last_digit = cal_row[char]
                break
        
        calibration_values.append(int(str(first_digit) + str(last_digit)))
    
    print(sum(calibration_values))
