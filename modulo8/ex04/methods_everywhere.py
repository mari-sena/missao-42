#!/usr/bin/env python3

import sys

def shrink(string):
    print(string[0:8])

def enlarge(string):
    final_result = ''
    index = len(string)

    for element in string:
        final_result += element
    while index <= 8:
        final_result += 'Z'
        index += 1

    return final_result

if len(sys.argv) < 2:
    print('none')
else:
    for element in sys.argv[1:]:
        if len(element) > 8:
            shrink(element)
        elif len(element) == 8:
            print(element)
        else:
            print(enlarge(element))
