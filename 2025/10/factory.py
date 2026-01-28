from itertools import combinations
from dataclasses import dataclass


@dataclass
class Machine:
    lights: list[int]
    buttons: list[tuple[int]]
    joltages: set[int]

    def press(self):
        lights = len(self.lights)
        for presses in range(1, len(self.buttons)+1):
            for combo in combinations(self.buttons, presses):
                state = [0] * lights

                for button in combo:
                    for light in button:
                        state[light] ^= 1

                if state == self.lights:
                    return presses


def parse(line):
    parts = line.strip().split()

    joltages = eval(parts.pop())
    
    lights = [
        1 if char == '#' else 0 
        for char in parts[0][1:-1]
        ]
    buttons = [
        tuple(map(int, part[1:-1].split(',')))
        for part in parts[1:]  
        ]
    
    return lights, buttons, joltages


with open("input.txt", "r") as file:
    machines = [Machine(*parse(line)) for line in file]

total = sum(machine.press() for machine in machines)

print(total)
