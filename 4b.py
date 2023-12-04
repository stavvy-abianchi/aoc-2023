from modules.input import read_input
from collections import Counter

def check_card(card_idx):
    wins = score_map[card_idx]
    if wins != 0:
        for won_cards in range(card_idx + 1, card_idx + wins + 1):
            cards_to_process.append(won_cards)
            card_count[won_cards] += 1

if __name__ == "__main__":
    game_data = read_input(__file__)

    scores = []
    score_map = {}
    cards_to_process = []

    card_count = {item: 0 for item in range(0, len(game_data))}
    for ticket in range(0, len(game_data)):
        card_num, raw_numbers = game_data[ticket].split(":")
        card_num = card_num.split(" ")[1]
        winning_nums, card_nums = raw_numbers.split("|")
        winning_nums = list(set(winning_nums.strip().split(" ")))
        card_nums = list(set(card_nums.strip().split(" ")))

        wins = [num for num in card_nums if num in winning_nums and num is not ""] # damn blanks!

        card_count[ticket] +=1
        score_map[ticket] = len(wins)
        if len(wins) != 0:
            for won_cards in range(ticket + 1, ticket + len(wins) + 1):
                cards_to_process.append(won_cards)
                card_count[won_cards] += 1
    
    while len(cards_to_process) > 0:
        card = cards_to_process.pop()
        check_card(card)

    print(card_count)
    print(sum(card_count.values()))