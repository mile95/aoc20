with open("input.txt") as f:
    entries = f.read().splitlines()

# Part A:
x_vels = [3]
y_vels = [1]

# Part B:
x_vels = [1,3,5,7,1]
y_vels = [1,1,1,1,2]

total = 1
for x_vel, y_vel in zip(x_vels, y_vels):
    x = trees =  0
    for entrie in entries[::y_vel]:
        while x >= len(entrie):
            entrie += entrie
        trees += entrie[x] == '#'
        x += x_vel
    total *= trees

print(total)

