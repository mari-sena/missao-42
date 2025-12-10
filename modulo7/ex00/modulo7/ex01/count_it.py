#!/usr/bin/env python3

import sys

arg_qty = len(sys.argv)

if arg_qty < 2:
    print('none')
else:
    index = 0
    while index < arg_qty:
        if index == 0:
            print(f'parameters: {len(sys.argv[1:])}')
        else:
            print(f'{sys.argv[index]}: {len(sys.argv[index])}')
        index += 1
    