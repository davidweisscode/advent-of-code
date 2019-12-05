# --- Day 4: Secure Container ---
# https://adventofcode.com/2019/day/4

def has_double_digit(pw):
    dd = False
    recent_digit = -1
    for digit in pw:
        if digit == recent_digit:
            dd = True
            break
        else:
            recent_digit = digit
    return dd

def is_not_decreasing(pw):
    nd = True
    lowest_digit = pw[0]
    for i in range(1, 6):
        if pw[i] < lowest_digit:
            nd = False
        elif pw[i] > lowest_digit:
            lowest_digit = pw[i]
    return nd

def has_true_double(pw):
    multiples = get_multiples(pw)
    return 2 in multiples
    

def get_multiples(pw):
    latest_digit = pw[0]
    multiple_counter = 1
    multiples = []
    for i in range(1, len(pw)):
        if pw[i] == latest_digit:
            multiple_counter += 1
            if i == len(pw) - 1:
                multiples.append(multiple_counter)
        else:
            multiples.append(multiple_counter)
            multiple_counter = 1
            latest_digit = pw[i]
    return multiples

start = 333333 #307237 # Lowest possible
end = 699999 #769058 # Highest possible

counter = 0

for pw in range(start, end + 1):
    dd = has_double_digit(str(pw))
    nd = is_not_decreasing(str(pw))
    td = has_true_double(str(pw))
    print(pw, dd, nd, td)
    if dd and nd and td:
        counter += 1

print(counter, "different passwords within the given range meet the criteria.")
