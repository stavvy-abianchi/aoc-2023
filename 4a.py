from modules.input import read_input
from collections import Counter


if __name__ == "__main__":
    game_data = read_input(__file__)

    scores = []
    for ticket in game_data:
        card_num, raw_numbers = ticket.split(":")
        card_num = card_num.split(" ")[1]
        winning_nums, card_nums = raw_numbers.split("|")
        winning_nums = list(set(winning_nums.strip().split(" ")))
        card_nums = list(set(card_nums.strip().split(" ")))

        wins = [num for num in card_nums if num in winning_nums and num is not ""] # damn blanks!

        if len(wins) != 0:
            scores.append( 2 ** (len(wins) - 1))
        else:
            print("no wins")

    print(sum(scores))
