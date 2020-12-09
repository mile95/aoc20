with open("input.txt") as f:
    entries = f.read().splitlines()

def run(instructions):
    acc = 0
    visited = set()
    pointer = 0
    prev_pointer = 0
    while(True):
        if pointer == len(instructions):
            return acc, True
        if pointer in visited:
            return acc, False
        visited.add(pointer)
        try:
            ins, val = tuple(instructions[pointer].split())
        except IndexError:
            return acc, False
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
    
    
print(f'A: {run(entries)}')

# Part B
change_index = 0
while(change_index <= len(entries)):
    entries_copy = entries.copy()
    ins, val = tuple(entries_copy[change_index].split())
    if ins == 'nop':
        entries_copy[change_index] = f'jmp {val}'
    elif ins == 'jmp':
        entries_copy[change_index] = f'nop {val}'
    else:
        change_index += 1
        continue

    acc, done = run(entries_copy)
    if done:
        print(f'B: {acc, done}')
        break
    change_index += 1
    
    

        
