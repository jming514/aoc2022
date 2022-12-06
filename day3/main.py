# PART 1
from collections import Counter


f = open("input.txt", "r")

sum = 0

for line in f:
    mid = len(line) // 2
    left = line[:mid]
    right = line[mid:]

    for letter in left:
        if right.find(letter) > -1:
            charCode = ord(letter)
            if charCode > 96:
                sum += charCode - 96
            else:
                sum += charCode - 38
            break

print(sum)

# PART 2
f = open("input.txt", "r")

sum = 0
arr = []

for idx, line in enumerate(f, start=1):
    arr.append(line.strip())

    # get 3 lines then operate
    if len(arr) == 3:
        a = Counter(arr[0])
        b = Counter(arr[1])
        c = Counter(arr[2])
        a = a & b
        a = a & c

        for letter in a:
            charCode = ord(letter)
            if charCode > 96:
                sum += charCode - 96
            else:
                sum += charCode - 38
            break


    # clear list before getting next 3 lines
    if idx % 3 == 0:
        arr.clear()

print(sum)
