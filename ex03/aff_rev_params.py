#!/usr/bin/env python3
import sys

if len(sys.argv) <= 2:
    print('none')
else:
    index = len(sys.argv) - 1
    while index > 0:
        first_param = sys.argv[index]
        print(first_param)
        index -= 1