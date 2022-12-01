with open("/workspaces/advent-of-code/2022/01-input.txt", "r") as lines:
    calorie_sum_list = []
    calorie_sum = 0
    for line in lines:
        if line == "\n":
            calorie_sum_list.append(calorie_sum)
            calorie_sum = 0
        else:
            calorie_sum += int(line)
    calorie_sum_list.append(calorie_sum)
    print(sum(sorted(calorie_sum_list)[-3:]))
