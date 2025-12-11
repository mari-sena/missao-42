#!/usr/bin/env python3

def greetings(*name):
    if str(*name) == '':
        print('Hello, noble stranger.')
    elif "int" in str(type(*name)):
        print('Error! It was not a name.')
    else:
        print('Hello, ' + str(*name) + '.')

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)