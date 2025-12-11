#!/usr/bin/env python3

def array_de_nomes(pessoas):
    for pessoa in pessoas:
        print(f'{pessoa.capitalize()}: {pessoas[pessoa].capitalize()}')

pessoas = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

array_de_nomes(pessoas)