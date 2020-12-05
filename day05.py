with open("input.txt") as f:
    entries = f.read().splitlines()

# Part A

seat_ids = []

for entry in entries:
    rows = list(range(0,128))
    for c in entry[:7]:
        rows = rows[:len(rows)//2] if c == 'F' else rows[len(rows)//2:] 
    seats = list(range(0,8))
    for c in entry[7:]:
        seats = seats[:len(seats)//2] if c == 'L' else seats[len(seats)//2:]
    seat_ids.append(rows[0]*8 + seats[0])  

print(max(seat_ids))

# Part B

print(set(range(min(seat_ids), max(seat_ids))).difference(set(seat_ids)))
        