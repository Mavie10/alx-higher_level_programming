#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

print("Last digit of", number, "is", abs(number) % 10, end=", ")

if abs(number) % 10 > 5:
    print("is greater than 5")
elif abs(number) % 10 == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")
