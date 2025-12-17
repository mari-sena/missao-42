#!/usr/bin/env python3

import sys

arg_qty = len(sys.argv)

if arg_qty != 3:
    print('none')
else:
    if sys.argv[1] > sys.argv[2]:
        print('O primeiro numero deve ser menor que o segundo')
        sys.exit()
    
    result = list(range(int(sys.argv[1]), int(sys.argv[2]) + 1))
    print(result)

    # Achei bacana:
    # result = []
    # index = int(sys.argv[1])
    # while index <= int(sys.argv[2]):
    #     result.append(index)
    #     index += 1