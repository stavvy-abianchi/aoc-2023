from modules.input import read_input
from functools import cmp_to_key
from operator import * 

def get_hand_type(hand):
    print(hand)
    hand_dict = {}
    for char in hand:
        if char not in hand_dict:
            hand_dict[char] = 1
        else:
            hand_dict[char] += 1
    hand_val = 0
    joker_count = hand_dict.get("J", 0)
    hand_dict = {k: v for k, v in hand_dict.items() if k != 'J'}

    if 5 in hand_dict.values():
        hand_val = 7
    elif 4 in hand_dict.values():
        hand_val = 6 if joker_count == 0 else 7
    elif 3 in hand_dict.values() and 2 in hand_dict.values():
        hand_val = 5
    elif 3 in hand_dict.values():
        if joker_count == 0:
            hand_val = 4
        if joker_count == 1:
            hand_val = 6
        if joker_count == 2:
            hand_val = 7
    elif countOf(hand_dict.values(), 2) > 1:
        hand_val = 3 if joker_count == 0 else 5
    elif 2 in hand_dict.values():
        if joker_count == 0:
            hand_val = 2
        if joker_count == 1:
            hand_val = 4
        if joker_count == 2:
            hand_val = 6
        if joker_count == 3:
            hand_val = 7
    else:
        if joker_count == 0:
            hand_val = 1
        if joker_count == 1:
            hand_val = 2
        if joker_count == 2:
            hand_val = 4
        if joker_count == 3:
            hand_val = 6
        if joker_count == 4:
            hand_val = 7

    if joker_count == 5:
        hand_val = 7
    
    return hand_val
    

def get_char_val(char):
    if char.isdigit():
        return int(char)
    elif char == 'T':
        return 10
    elif char == 'J':
        return 1
    elif char == 'Q':
        return 12
    elif char == 'K':
        return 13
    elif char == 'A':
        return 14

def compare_hands(hand1, hand2):
    rank1 = get_hand_type(hand1[0])
    rank2 = get_hand_type(hand2[0])

    if rank1 == rank2:
        for char_idx in range(0, len(hand1[0])):
            char1 = hand1[0][char_idx]
            char2 = hand2[0][char_idx]

            if get_char_val(char1) == get_char_val(char2):
                continue
            else:
                return get_char_val(char1) - get_char_val(char2)
    else:
        return rank1 - rank2

if __name__ == "__main__":
    game_data = read_input(__file__)

    bids = []

    for dealt_hand in game_data:
        hand, bid = dealt_hand.split(" ")
        bids.append((hand, int(bid)))
    
    results = sorted(bids, key=cmp_to_key(compare_hands))
    final_score = 0

    for bid_idx in range(0, len(results)):
        final_score += results[bid_idx][1] * (bid_idx + 1)
    
    print(final_score)
