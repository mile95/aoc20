import json

with open("input.txt") as f:
    entries = f.read().splitlines()

# Part A

# Find indicies with empty lines to make it easy to merge correct entries.
indices = [i for i, x in enumerate(entries) if x == ''] + [len(entries)]

# Collect all passports as seperate strings
passports = []
idx_from = 0
for idx_to in indices:
    passports.append(' '.join(entries[idx_from:idx_to]))
    idx_from = idx_to

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
count = 0
for passport in passports:
    count += sum([field in passport for field in required_fields]) == 7
print(count)

# Part B
count = 0
for passport in passports:
    passport_pars = passport.split()
    valid = True
    for part in passport_pars:
        key, value = tuple(part.split(':'))
        if key == 'byr':
            valid = valid and 1920 <= int(value) <= 2002
        elif key == 'iyr':
            valid = valid and 2010 <= int(value) <= 2020
        elif key == 'eyr':
            valid = valid and 2020 <= int(value) <= 2030
        elif key == 'hgt':
            if value[-2:] == 'cm':
                valid = valid and 150 <= int(value[:-2]) <= 193
            elif value[-2:] == 'in':
                valid = valid and 59 <= int(value[:-2]) <= 76
            else:
                valid = False
        elif key == 'hcl':
            if value[0] == '#':
                valid = valid and (len(value) == 7)
                for c in value[1:]:
                    valid = valid and (c in "abcdef" or c in "0123456789")
            else:
                valid = False          
        elif key == 'ecl':
            valid = valid and value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif key == 'pid':
            valid = valid and len(value) == 9 and value.isnumeric()
        elif key == 'cid':
            valid = valid and True
        else:
            valid = False

    count+=valid
                 
print(count)