#!/usr/bin/env python3

import sys

arg_qty = len(sys.argv)

if arg_qty < 2:
    print('none')
else:
    index = 1
    while index < arg_qty:
        param = sys.argv[index]
        param_qty = len(sys.argv)
        check_start_by = param.find('ism')
        if check_start_by == -1:
            print(f'{param}ism')
        index += 1