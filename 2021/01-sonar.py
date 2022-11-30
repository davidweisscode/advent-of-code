# --- Day 1: Sonar Sweep ---
# https://adventofcode.com/2021/day/1

import math

def count_increases(numbers):
    """
    Returns number of times the next integer increases
    """
    counter = 0
    last = math.inf
    current = 0
    while numbers:
        current = numbers.pop(0)
        if current > last:
            counter += 1
        last = current
    return counter

with open("01-input.txt", "r") as depths:
    print(count_increases(list(map(int, depths))))
