#!/usr/bin/env python3

import sys

arg_qty = len(sys.argv)

if arg_qty < 2:
    print('none')
else:
    index = 0
    param_len = len(sys.argv[1])
    z_qty = ''
    while index <= param_len - 1:
        if sys.argv[1][index] == 'z':
            z_qty += 'z'
        index += 1
    print(f'{z_qty}')
