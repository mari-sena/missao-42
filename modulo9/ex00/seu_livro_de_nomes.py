#!/usr/bin/env python3

def array_de_nomes(pessoas):
    result = []
    for pessoa in pessoas:
        aux = str(pessoa.capitalize()) + ': ' + str(pessoas[pessoa].capitalize())
        result.append(aux)
    return result
    

pessoas = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_de_nomes(pessoas))