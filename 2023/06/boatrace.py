#Time:        44     70     70     80
#Distance:   283   1134   1134   1491

records = {44: 283, 70: 1134, 80: 1491}

win_multi = 1

for racetime in (44, 70, 70, 80):
    wins = 0
    for hold in range(1, racetime):
        remaining_time = racetime - hold
        if hold * remaining_time > records[racetime]:
            wins += 1
    win_multi *= wins

print(win_multi)