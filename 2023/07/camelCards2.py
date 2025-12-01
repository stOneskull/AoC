from collections import Counter

with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

hand_ranks = {
    'highcard': 1,
    '1pair': 2,
    '2pair': 3,
    '3kind': 4,
    'fullhouse': 5,
    '4kind': 6,
    '5kind': 7
}

pic_convert = {
    'T': 10,
    'J': 1, #wild
    'Q': 12,
    'K': 13,
    'A': 14
}

def convert(hand):
    converted = []
    for card in hand:
        if card in pic_convert:
            converted.append(pic_convert[card])
        else:
            converted.append(int(card))
    return converted


def find_hand(hand):
    joker_count = hand.count(1)

    if joker_count == 5:
        return '5kind'

    non_jokers = [card for card in hand if card > 1]
    
    counts = Counter(non_jokers)
    sorted_counts = sorted(counts.values(), reverse=True)

    sorted_counts[0] += joker_count

    if sorted_counts[0] == 5:
        return '5kind'
    if sorted_counts[0] == 4:
        return '4kind'
    if sorted_counts[0] == 3 and sorted_counts[1] == 2:
        return 'fullhouse'
    if sorted_counts[0] == 3:
        return '3kind'
    if sorted_counts[0] == 2 and sorted_counts[1] == 2:
        return '2pair'
    if sorted_counts[0] == 2:
        return '1pair'
    else:
        return 'highcard'
    

all_hands = []

for line in lines:
    hand, bid = line.split()
    converted_hand = convert(hand)
    hand_type = find_hand(converted_hand)
    all_hands.append((hand_ranks[hand_type], converted_hand, int(bid)))

all_hands.sort()

total = 0
for rank, (_, _, bid) in enumerate(all_hands, start=1):
    total += rank * bid

print(total)
