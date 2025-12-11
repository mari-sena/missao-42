#!/usr/bin/env python3

import sys

def downcase_it(string):
    return string.lower()

if len(sys.argv) < 2:
    print('none')
else:
    for element in sys.argv[1:]:
        print(downcase_it(element))
