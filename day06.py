with open("input.txt") as f:
    entries = f.read().split('\n\n')


# Part A
answers = [entry.replace('\n','') for entry in entries]
count = sum(len(set(x)) for x in answers)
print(count)


# Part B
count = 0
answers = [x.split() for x in entries]
for answer in answers:
    intersection_set = set(answer[0])
    for a in answer[1:]:
        intersection_set = intersection_set & set(a)
    count+= len(intersection_set)
print(count)