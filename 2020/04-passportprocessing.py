import re
import unittest

class TestFieldValidation(unittest.TestCase):

    def setUp(self):
        self.valid_passport_string = "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f"
        self.valid_passport = format_passport(self.valid_passport_string)
        self.invalid_passport_string = "eyr:1972 cid:100 hcl:#123abz ecl:wat hgt:190in pid:0123456789 iyr:2021 byr:2003"
        self.invalid_passport = format_passport(self.invalid_passport_string)

    def test_byr(self):
        self.assertTrue(byr(self.valid_passport))
        self.assertFalse(byr(self.invalid_passport))

    def test_iyr(self):
        self.assertTrue(iyr(self.valid_passport))
        self.assertFalse(iyr(self.invalid_passport))

    def test_eyr(self):
        self.assertTrue(eyr(self.valid_passport))
        self.assertFalse(eyr(self.invalid_passport))

    def test_hgt(self):
        self.assertTrue(hgt(self.valid_passport))
        self.assertFalse(hgt(self.invalid_passport))

    def test_hcl(self):
        self.assertTrue(hcl(self.valid_passport))
        self.assertFalse(hcl(self.invalid_passport))

    def test_ecl(self):
        self.assertTrue(ecl(self.valid_passport))
        self.assertFalse(ecl(self.invalid_passport))

    def test_pid(self):
        self.assertTrue(pid(self.valid_passport))
        self.assertFalse(pid(self.invalid_passport))

inputstr = ""
with open("04-input.txt", "r") as file:
    for line in file:
        inputstr += line

# --- Part 1 --- Count the number of valid passports - those that have all required fields. Treat cid as optional.

REQUIRED = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

def get_passports(str):
    return str.split("\n\n")

def format_passport(str):
    passportstr = str.replace("\n", " ")
    fields = passportstr.split(" ")
    passport = dict()
    for field in fields:
        key = field.split(":")[0]
        val = field.split(":")[1]
        passport[key] = val
    return passport

def validate(str):
    valid = 0
    passports = get_passports(str)
    for passport in passports:
        passport = format_passport(passport)
        present_fields = set()
        for field in passport:
            present_fields.add(field)
        if REQUIRED.issubset(present_fields):
            valid += 1
    return valid

# --- Part 2 --- Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional.

def byr(p):
    # byr (Birth Year)       - four digits; at least 1920 and at most 2002.
    try:
        return int(p["byr"]) in range(1920, 2003)
    except KeyError:
        return False

def iyr(p):
    # iyr (Issue Year)       - four digits; at least 2010 and at most 2020.
    try:
        return int(p["iyr"]) in range(2010, 2021)
    except KeyError:
        return False

def eyr(p):
    # eyr (Expiration Year)  - four digits; at least 2020 and at most 2030.
    try:
        return int(p["eyr"]) in range(2020, 2031)
    except KeyError:
        return False

def hgt(p):
    # hgt (Height)           - a number followed by either cm or in:
    #                            If cm, the number must be at least 150 and at most 193.
    #                            If in, the number must be at least 59 and at most 76.
    try:
        if p["hgt"][-2:] == "cm":
            return int(p["hgt"][:-2]) in range(150, 194)
        elif p["hgt"][-2:] == "in":
            return int(p["hgt"][:-2]) in range(59, 77)
    except KeyError:
        return False

def hcl(p):
    # hcl (Hair Color)       - a # followed by exactly six characters 0-9 or a-f.
    try:
        match = re.search(r'^#[0-9a-f]{6}', p["hcl"])
        if match:
            return True
        else:
            return False
    except KeyError:
        return False

def ecl(p):
    # ecl (Eye Color)        - exactly one of: amb blu brn gry grn hzl oth.
    try:
        return p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    except KeyError:
        return False

def pid(p):
    # pid (Passport ID)      - a nine-digit number, including leading zeroes.
    try:
        match = re.search(r'^[0-9]{9}$', p["pid"])
        if match:
            return True
        else:
            return False
    except KeyError:
        return False

# cid (Country ID)       - ignored, missing or not.
def cid(p):
    pass

def validate_strict(str):
    valid = 0
    passports = get_passports(str)
    for p in passports:
        p = format_passport(p)
        if byr(p) and iyr(p) and eyr(p) and hgt(p) and hcl(p) and ecl(p) and pid(p):
            valid += 1
    return valid

if __name__ == '__main__':
    print(f"{validate(inputstr)} passports are valid for schema 1.")
    print(f"{validate_strict(inputstr)} passports are valid for schema 2.")
    unittest.main()
