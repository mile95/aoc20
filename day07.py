import re
import collections

with open("input.txt") as f:
    entries = f.read().splitlines()

first_regex = re.compile('^(\w+ \w+) bags contain (.+)$')
second_regex = re.compile('(\d+) (\w+ \w+)')

network = collections.defaultdict(list)
for entry in entries:
    matches = first_regex.match(entry)
    parent = matches[1]
    for _, child in second_regex.findall(matches[2]):
        network[child].append(parent)

def compute_A(color):
    s = {color}
    for parent in network[color]:
        s |= compute_A(parent)
    return s

# Part A
print(len(compute_A('shiny gold')) - 1)

# Part B
network = {}
for entry in entries:
    matches = first_regex.match(entry)
    parent = matches[1]
    children = []
    for d, child in second_regex.findall(matches[2]):
        children.append((int(d), child))
    network[parent] = children

def compute_B(n, color):
    count = n
    for child_n, child in network[color]:
        count += compute_B(n*child_n, child)
    return count

print(compute_B(1, 'shiny gold') - 1)