#thanks for the help, gemini!

from dataclasses import dataclass

from scipy.optimize import linprog


@dataclass
class Machine:
    lights: list[int]
    buttons: list[tuple[int]]
    joltages: list[int]

    def joltage_press(self):
        buttons = len(self.buttons)
        counters = len(self.joltages)

        # The cost for each button press. We set it to 1 for all buttons
        # to tell the solver our objective is to minimize the total number of presses.
        cost_per_press = [1] * buttons

        # This matrix maps which buttons affect which counters.
        # Each row is a counter, each column is a button.
        # button_counter_map[j, i] = 1 if button i affects counter j.
        button_counter_map = [[0] * buttons for _ in range(counters)]
        for i, button in enumerate(self.buttons):
            for counter in button:
                if counter < counters:
                    button_counter_map[counter][i] = 1

        # This vector holds the target joltage for each counter.
        target_joltages = self.joltages

        # Solve the integer linear programming problem.
        res = linprog(cost_per_press, A_eq=button_counter_map, b_eq=target_joltages, bounds=(0, None), integrality=1)
        return int(round(res.fun)) if res.success else 0

def parse(line):
    parts = line.strip().split()

    joltages_str = parts.pop()
    
    lights = [
        1 if char == '#' else 0 
        for char in parts[0][1:-1]
        ]
    buttons = [
        tuple(map(int, part[1:-1].split(',')))
        for part in parts[1:]  
        ]

    # Manually parse joltages to preserve order, e.g., '{3,5,4,7}'
    joltages_content = joltages_str.strip()[1:-1]
    joltages = [int(j) for j in joltages_content.split(',')] if joltages_content else []
    
    return lights, buttons, joltages


with open("input.txt", "r") as file:
    machines = [Machine(*parse(line)) for line in file]

total = sum(machine.joltage_press() for machine in machines)

print(total)
