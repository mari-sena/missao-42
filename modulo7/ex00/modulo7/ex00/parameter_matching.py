#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print('none')
    sys.exit()

param_to_validate = input('What was the parameter? ')

if sys.argv[1] == param_to_validate:
    print("Good job!")
else:
    print('Nope, sorry...')