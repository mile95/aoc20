from itertools import permutations

with open("input.txt") as f:
    entries = f.readlines()
    entries = [int(x.strip()) for x in entries]

a = [a*b for a,b in permutations(entries, 2) if sum((a,b)) == 2020]
b = [a*b*c for a,b,c in permutations(entries, 3) if sum((a,b,c)) == 2020]
print(a[0])
print(b[0])