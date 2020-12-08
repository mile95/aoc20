with open("input.txt") as f:
    entries = f.read().splitlines()

acc = 0
visited = []
pointer = 0
prev_pointer = 0

# Part A
while(True):
    if pointer in visited:
        break
    visited.append(pointer)
    ins, val = tuple(entries[pointer].split())
    if ins == 'nop':
        prev_pointer = pointer
        pointer+=1
    if ins == 'acc':
        prev_pointer = pointer
        acc+=int(val)
        pointer+=1
    if ins == 'jmp':
        prev_pointer = pointer
        pointer+=int(val)
    
    

print(f'A: {acc}')

# Part B

print(prev_pointer)
ins, val = tuple(entries[prev_pointer].split())
if ins == 'jmp':
    entries[prev_pointer] = f'nop {val}'
if ins == 'nop':
    entries[prev_pointer] = f'jmp {val}'

acc = 0
visited = []
pointer = 0
prev_pointer = 0
while(True):
    if pointer in visited:
        break
    visited.append(pointer)
    ins, val = tuple(entries[pointer].split())
    if ins == 'nop':
        pointer+=1
    if ins =='acc':
        acc+=int(val)
        pointer+=1
    if ins == 'jmp':
        pointer+=int(val)

print(f'B: {acc}')