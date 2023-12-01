from modules.input import read_input
import re

def has_words_left(word_dict: dict):
    for val in word_dict.values():
        if len(val) > 0:
            return True
    
    return False

def find_digits(cal_row):
    first_digit_index = None
    last_digit_index = None

    for char in range(0, len(cal_row)):
        if (cal_row[char].isdigit()):
            first_digit_index = char
            break

    for char in range(len(cal_row) -1, -1, -1):
        if (cal_row[char].isdigit()):
            last_digit_index = char
            break
    
    return first_digit_index, last_digit_index

def find_digit_words(cal_row, word_map):
    for num_word in word_map.keys():
        matches = re.finditer(num_word, cal_row)
        num_match = sum(1 for _ in matches)

        index_num_word[num_word] = []
        if num_match > 0:
            for match in re.finditer(num_word, cal_row):
                index_num_word[num_word].append(match.start())

    if (has_words_left(index_num_word)):
        possible_index = [x for x in index_num_word.values() if len(x) > 0]
        flat_index = [x for n in possible_index for x in n]
        min_index = min(i for i in flat_index if i > -1)
        max_index = max(i for i in flat_index if i > -1)
        min_num = word_map[[key for key in index_num_word if min_index in index_num_word[key]][0]][0]
        max_num = word_map[[key for key in index_num_word if max_index in index_num_word[key]][0]][0]
        return min_index, min_num, max_index, max_num
    else:
        return None, None, None, None

if __name__ == "__main__":
    input = read_input(__file__)

    calibration_values = []
    word_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    for cal_row in input:
        index_num_word = {key:None for key in word_map.keys()}
        min_d, max_d = find_digits(cal_row)
        min_word_index, min_word, max_word_index, max_word = find_digit_words(cal_row, word_map)

        first_digit_index = min(x for x in [min_d, min_word_index] if x is not None)
        last_digit_index = max(x for x in [max_d, max_word_index] if x is not None)

        first_digit = cal_row[first_digit_index] if cal_row[first_digit_index].isdigit() else min_word
        last_digit = cal_row[last_digit_index] if cal_row[last_digit_index].isdigit() else max_word

        calibration_values.append(int(str(first_digit) + str(last_digit)))

    print(sum(calibration_values))
