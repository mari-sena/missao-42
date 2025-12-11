#!/usr/bin/env python3

import sys

arg_qty = len(sys.argv)

if arg_qty < 2:
    print('none')
else:
    for index, element in enumerate(sys.argv):
        if index == 0:
            print(f'parameters: {len(sys.argv[1:])}')
        else:
            print(f'{element}: {len(element)}')
