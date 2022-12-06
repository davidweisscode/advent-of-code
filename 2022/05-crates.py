with open("/workspaces/advent-of-code/2022/05-input.txt", "r", encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

# [Q] [J]                         [H]
# [G] [S] [Q]     [Z]             [P]
# [P] [F] [M]     [F]     [F]     [S]
# [R] [R] [P] [F] [V]     [D]     [L]
# [L] [W] [W] [D] [W] [S] [V]     [G]
# [C] [H] [H] [T] [D] [L] [M] [B] [B]
# [T] [Q] [B] [S] [L] [C] [B] [J] [N]
# [F] [N] [F] [V] [Q] [Z] [Z] [T] [Q]
#  1   2   3   4   5   6   7   8   9 

stacks = [
    ["F", "T", "C", "L", "R", "P", "G", "Q", ],
    ["N", "Q", "H", "W", "R", "F", "S", "J", ],
    ["F", "B", "H", "W", "P", "M", "Q", ],
    ["V", "S", "T", "D", "F", ],
    ["Q", "L", "D", "W", "V", "F", "Z", ],
    ["Z", "C", "L", "S", ],
    ["Z", "B", "M", "V", "D", "F", ],
    ["T", "J", "B", ],
    ["Q", "N", "B", "G", "L", "S", "P", "H", ],
]

for line in lines[10:]:
    instruction = line.split(" ")
    repeats = int(instruction[1])
    from_stack = int(instruction[3])
    to_stack = int(instruction[5])
    print(line)
    print(repeats, from_stack, to_stack)
    for _ in range(repeats):
        crate = stacks[from_stack - 1].pop()
        stacks[to_stack - 1].append(crate)
    print()

[print(stack.pop(), end="") for stack in stacks]

#########################

stacks = [
    ["F", "T", "C", "L", "R", "P", "G", "Q", ],
    ["N", "Q", "H", "W", "R", "F", "S", "J", ],
    ["F", "B", "H", "W", "P", "M", "Q", ],
    ["V", "S", "T", "D", "F", ],
    ["Q", "L", "D", "W", "V", "F", "Z", ],
    ["Z", "C", "L", "S", ],
    ["Z", "B", "M", "V", "D", "F", ],
    ["T", "J", "B", ],
    ["Q", "N", "B", "G", "L", "S", "P", "H", ],
]

for line in lines[10:]:
    instruction = line.split(" ")
    amount = int(instruction[1])
    from_stack = int(instruction[3])
    to_stack = int(instruction[5])
    print(line)
    print(amount, from_stack, to_stack)
    crates = stacks[from_stack - 1][-amount:]
    del stacks[from_stack - 1][-amount:]
    stacks[to_stack - 1].extend(crates)
    print()

[print(stack.pop(), end="") for stack in stacks]
