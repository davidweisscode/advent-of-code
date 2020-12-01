# --- Day 1: The Tyranny of the Rocket Equation ---
# https://adventofcode.com/2019/day/1

def get_fuel(mass):
    if (mass // 3 - 2) < 0:
        return 0
    else:
        return (mass // 3 - 2) + get_fuel(mass // 3 - 2)

total_fuel = 0
with open("modules.txt", "r") as modules:
    for module in modules:
        total_fuel += get_fuel(int(module))
print(total_fuel)
