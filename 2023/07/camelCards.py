with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

handbook = {
    '5kind': [],
    '4kind': [],
    'fullhouse': [],
    '3kind': [],
    '2pair': [],
    '1pair': [],
    'highcard': []
}

pic_convert = {
    'T': 10,
    'J': 11,
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


def hand2handbook(hand, bid):
    global handbook

    uniques = len(set(hand))
    if uniques == 1:
        handbook['5kind'].append((hand, bid))
    elif uniques == 2:
        if hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4:
            handbook['4kind'].append((hand, bid))
        else:
            handbook['fullhouse'].append((hand, bid))
    elif uniques == 3:
        if hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3:
            handbook['3kind'].append((hand, bid))
        else:
            handbook['2pair'].append((hand, bid))
    elif uniques == 4:
        handbook['1pair'].append((hand, bid))
    else:
        handbook['highcard'].append((hand, bid))
    
    
for line in lines:
    hand, bid = line.split()
    hand2handbook(convert(hand), int(bid))

for eachtype in handbook:
    handbook[eachtype].sort(reverse=True)

all_hands = []
for eachtype in handbook:
    all_hands.extend(handbook[eachtype])

all_hands = reversed(all_hands)

total = 0
for rank, (_, bid) in enumerate(all_hands, start=1):
    total += rank * bid

print(total)
