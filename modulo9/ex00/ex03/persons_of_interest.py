#!/usr/bin/env python3

def famous_births(dicionario):
    lista_de_itens = dicionario.items()
    itens_ordenados = sorted(lista_de_itens, key=lambda item_tupla:item_tupla[1]['date_of_birth'])
    for chave_interna, dados_pessoa in itens_ordenados:
        nome = dados_pessoa['name']
        data_nascimento = dados_pessoa['date_of_birth']
        print(f"{nome} is a great scientist born in {data_nascimento}")

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)