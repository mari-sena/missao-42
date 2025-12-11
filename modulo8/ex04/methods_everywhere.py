#!/usr/bin/env python3

import sys

def shrink(string):
    print(string[8:])

def enlarge(string):
    return 'f'

if len(sys.argv) < 2:
    print('none')
else:
    if (len(string) > 7):
        shrink(sys.)