# PART 1
f = open("input.txt", "r")

total = 0

thisdict = {
    "A": 1,  # rock
    "B": 2,  # paper
    "C": 3,  # scissors
    "X": 1,  # rock
    "Y": 2,  # paper
    "Z": 3,  # scissors
}

for line in f:
    x = line.split()

    # draw
    if thisdict[x[0]] == thisdict[x[1]]:
        total += 3
    # next 3 are losing conditions
    elif x[0] == "A" and x[1] == "Z":
        total += 0
    elif x[0] == "B" and x[1] == "X":
        total += 0
    elif x[0] == "C" and x[1] == "Y":
        total += 0
    else:
        total += 6

    # add points based on pick
    total += thisdict[x[1]]

print(total)

# PART 2
f = open("input.txt", "r")

total = 0

# X = must lose
# Y = must draw
# Z = must win
newdict = {
    "A": 1,  # rock
    "B": 2,  # paper
    "C": 3,  # scissors
}

for line in f:
    x = line.split()

    if x[1] == "Y":
        total += 3  # points from draw
        total += newdict[x[0]]
    elif x[1] == "Z":
        total += 6  # points from win
        if x[0] == "C":
            total += 1
        else:
            total += newdict[x[0]] + 1
    else:
        if x[0] == "A":
            total += 3
        else:
            total += newdict[x[0]] - 1

print(total)

