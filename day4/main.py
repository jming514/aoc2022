import re

# PART 1
f = open("input.txt", "r")

total = 0

for line in f:
    arr = re.split("-|,",line.strip())
    arr = [int(x) for x in arr]

    if arr[0] <= arr[2] and arr[1] >= arr[3]:
        total += 1
    elif arr[0] >= arr[2] and arr[1] <= arr[3]:
        total += 1

print(total)

# PART 2
f = open("input.txt", "r")

total = 0

for line in f:
    arr = re.split("-|,",line.strip())
    arr = [int(x) for x in arr]

    if arr[0] <= arr[3] and arr[0] >= arr[2]:
        total += 1
    elif arr[1] <= arr[3] and arr[1] >= arr[2]:
        total += 1
    elif arr[0] <= arr[2] and arr[1] >= arr[3]:
        total += 1
    elif arr[0] >= arr[2] and arr[1] <= arr[3]:
        total += 1

print(total)
