#!/usr/bin/python3
for i in range(10):
    for l in range(i, 10):
        if i < l:
            print("{:d}{:d}".format(i, l), end="\n" if i == 8 and l == 9 else ", ")
