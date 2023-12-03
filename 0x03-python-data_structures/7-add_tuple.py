#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
if len(tuple_a) > 0 else 0
if len(tuple_a) > 1 else 0
if len(tuple_b) > 0 else 0
if len(tuple_b) > 1 else 0
    new_tuple = tuple (map(sum,zip(tuple_a, tuple_b)))
        print(new_tuple)
