import math

racetime = 44_707_080
distance = 283_113_411_341_491

# a win:
# hold * (time-hold) > distance
# time*hold - hold**2 > distance
# -hold**2 > distance - time*hold
# 0 > distance - time*hold + hold**2
# hold**2 - time*hold + distance < 0

# find the roots of: 
# hold**2 - time*hold + distance == 0
# quadratic formula: 
# x = (-b (+/-) sqrt(b**2 - 4ac)) / 2a
# hold = (time (+/-) sqrt(time**2 - 4*distance)) / 2

discriminant = racetime**2 - 4 * distance
sqrt_discriminant = math.sqrt(discriminant)

hold_lower = (racetime - sqrt_discriminant) / 2
hold_upper = (racetime + sqrt_discriminant) / 2

# (math.ceil(hold_upper) - 1) - (math.floor(hold_lower) + 1) + 1
# math.ceil(hold_upper) - 1 - math.floor(hold_lower) - 1 + 1
wins = math.ceil(hold_upper) - math.floor(hold_lower) - 1

print(wins)