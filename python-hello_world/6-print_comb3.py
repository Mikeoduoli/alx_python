#!/usr/bin/python3
for i in range(9):
    for j in range(1, 10):
        if i < j and i <= 8 and j <= 9:
            print("{:d}{:d}".format(i, j), end="")
            if i < 8 and j <= 9:
                print(", ", end="")
            else:
                print("\n", end="")
