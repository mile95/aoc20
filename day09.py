import itertools

with open("input.txt") as f:
    entries = f.read().splitlines()
    entries = [int(n) for n in entries]

PREASEMBLE_LENGTH = 25


# Part A
found = False
pointer = PREASEMBLE_LENGTH
bad_value = 0
while not found:
    history = entries[pointer-PREASEMBLE_LENGTH:pointer]
    next_value = entries[pointer]
    
    valid = False
    for history_value in history:
        if next_value - history_value in history:
            valid = True
            break
    if not valid:
        bad_value = next_value
        print(f'A: {bad_value}')
        found = True
    pointer += 1

# Part B

found = False
sp = 0
ep = 1
while not found:
    current_sum = sum(entries[sp:ep])
    if current_sum == bad_value:
        print(f'B: {max(entries[sp:ep]) + min(entries[sp:ep])}')
        break
    elif current_sum > bad_value:
        sp+=1
        ep = sp + 1
    else:
        ep+=1
