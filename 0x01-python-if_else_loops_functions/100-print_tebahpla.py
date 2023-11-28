#!/usr/bin/python3
for char_code in range(ord('z'), ord('a') - 1, -1):
    char = chr(char_code)
    case = 'lower' if char.islower() else 'upper'
    print(f"{char:{case}}", end='')
