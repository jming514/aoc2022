# part 1
# didn't actually need to get the index
f = open('part1.txt', 'r')

most = 0
current = 0
count = 0

for line in f:
    if line.strip():
        current += int(line)
    else:
        if current > most:
            count += 1
            most = current

        current = 0

if current > most:
    count += 1
    most = current

print(most)

# part 2
top1 = 0
top2 = 0
top3 = 0
current = 0

f = open('part1.txt', 'r')

for line in f:
    if line.strip():
        current += int(line)
    else:
        if current > top1:
            top3 = top2
            top2 = top1
            top1 = current
        elif current > top2:
            top3 = top2
            top2 = current
        elif current > top3:
            top3 = current

        current = 0

if current > top1:
    top3 = top2
    top2 = top1
    top1 = current
elif current > top2:
    top3 = top2
    top2 = current
elif current > top3:
    top3 = current

print(top1 + top2 + top3)
