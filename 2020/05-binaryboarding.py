import math

# --- Part 1 --- What is the highest seat ID on a boarding pass? ID = row * 8 + col, FBLR encode to consider first or second half of 128 rows and 8 cols

def get_seat_id(code):
    row_code = code[:7]
    col_code = code[7:]
    return decode_row(row_code) * 8 + decode_col(col_code)

def decode_row(splits):
    row = (0, 127)
    for split in splits:
        if split == "F":
            row = (row[0], row[1] - math.ceil((row[1] - row[0]) / 2))
        elif split == "B":
            row = (row[0] + math.ceil((row[1] - row[0]) / 2), row[1])
    if row[0] == row[1]:
        return row[0]

def decode_col(splits):
    col = (0, 7)
    for split in splits:
        if split == "L":
            col = (col[0], col[1] - math.ceil((col[1] - col[0]) / 2))
        elif split == "R":
            col = (col[0] + math.ceil((col[1] - col[0]) / 2), col[1])
    if col[0] == col[1]:
        return col[0]

# --- Part 2 --- What is the ID of your seat? It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well. Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

def find_missing_id(ids):
    # What ids are missing?
    ids = set(ids)
    possible_ids = set(range(0, 1024))
    missing_ids = possible_ids.difference(ids)

    # What of such missing ids have both their adjacent neighbors?
    for missing_id in missing_ids:
        if missing_id + 1 in ids and missing_id - 1 in ids:
            return missing_id

if __name__ == "__main__":
    with open("05-input.txt", "r") as codes:
        ids = []
        for code in codes:
            ids.append(get_seat_id(code))
        print(f"The highest seat ID is {max(ids)}")
        print(f"There are {len(ids)} boarding passes in the list. {128 * 8} total seats in the aircraft.")
        print(f"My missing ID is {find_missing_id(ids)}")
