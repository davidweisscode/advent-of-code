with open("/workspaces/advent-of-code/2022/04-input.txt", "r", encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]
    full_contains = 0
    overlaps = 0
    for line in lines:
        r_0 = line.split(",")[0] # assignment range of the first elf of a elf pair
        r_1 = line.split(",")[1]
        r_0_lower = int(r_0.split("-")[0])
        r_0_upper = int(r_0.split("-")[1])
        r_1_lower = int(r_1.split("-")[0])
        r_1_upper = int(r_1.split("-")[1])

        if r_0_lower >= r_1_lower and r_0_upper <= r_1_upper:
            full_contains += 1 # range 0 is fully contained by range 1
        elif r_0_lower <= r_1_lower and r_0_upper >= r_1_upper:
            full_contains += 1 # range 1 is fully contained by range 0

        r_0 = set(range(r_0_lower, r_0_upper + 1))
        r_1 = set(range(r_1_lower, r_1_upper + 1))
        if set.intersection(r_0, r_1):
            overlaps += 1
        
    print("The amount of full-contains in assignment ranges is", full_contains)
    print("The amount of overlaps is", overlaps)
