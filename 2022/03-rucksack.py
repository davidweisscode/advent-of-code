with open("/workspaces/advent-of-code/2022/03-input.txt", "r", encoding="utf-8") as file:
    itemtypes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    lines = [line.rstrip() for line in file]
    priority_sum = 0
    for line in lines:
        comp_1 = line[:len(line) // 2]
        comp_2 = line[len(line) // 2:]
        item = list(set(comp_1).intersection(set(comp_2)))[0]
        priority = itemtypes.index(item) + 1
        priority_sum += priority

        print(comp_1)
        print(set(comp_1))
        print(set(comp_2))
        print(item)
        print(priority)
    print("The sum of all priorities is", priority_sum)

    badge_priority_sum = 0
    while lines:
        rucksacks = lines[:3]
        del lines[:3] # Why cant .pop() pop multiple elements in Python?
        item = list(set.intersection(*map(set, rucksacks)))[0]
        badge_priority = itemtypes.index(item) + 1
        badge_priority_sum += badge_priority
    print("The sum of all badge priorities is", badge_priority_sum)
