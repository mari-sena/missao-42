#!/usr/bin/env python3

import sys

def add_one(num):
    print(num + 1)

variavel = sys.argv[1]
print(variavel)
add_one(int(sys.argv[1]))
print(variavel)