with open("input.txt") as f:
    entries = f.read().splitlines()

bags = {}
for entry in entries:
    bag = entry.split(' bags')[0] 
    value =  entry.split(' bags')[1].split(' contain')[1].replace('bag','')
    value_d = {}
    for x in value.strip().split(', '):
        if not x == 'no other':
            value_d[x.split(' ', 1)[1].replace('.','').strip()] = int(x.split(' ')[0])

    bags[bag] = value_d

print(bags)
