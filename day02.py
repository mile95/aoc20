with open("input.txt") as f:
    entries = f.readlines()

# Part A
count = 0
for entrie in entries:
    parts = entrie.rstrip().split(" ")
    min_n = int(parts[0].split("-")[0])
    max_n = int(parts[0].split("-")[1])
    c = parts[1].replace(":", "")
    password = parts[2]
    
    count = count + 1 if password.count(c) in range(min_n, max_n + 1) else count

print(f"A: {count}")
    
# Part B
count = 0
for entrie in entries:
    parts = entrie.rstrip().split(" ")
    # Toboggan Corporate Policies have no concept of "index zero"!
    first = int(parts[0].split("-")[0]) - 1
    last = int(parts[0].split("-")[1]) - 1
    c = parts[1].replace(":", "")
    password = parts[2]

    pos_one_valid = False
    pos_two_valid = False
    if len(password) > first : 
        pos_one_valid = password[first] == c
    if len(password) > last:
        pos_two_valid = password[last] == c

    count = count + 1 if (pos_one_valid + pos_two_valid) == 1 else count

print(f"B: {count}")