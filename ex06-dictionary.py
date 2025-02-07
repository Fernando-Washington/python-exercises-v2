# 6. Dicionário de números pares e ímpares

'''
Escreva uma função que receba uma lista de números inteiros e utilize lambda e
filter para dividir a lista em números pares e ímpares. Retorne um dicionário com
duas chaves: "pares" e "ímpares".

Exemplo de entrada: [1, 2, 3, 4, 5, 6]
Exemplo de saída: {"pares": [2, 4, 6], "ímpares": [1, 3, 5]}
'''

num_list = [1, 2, 3, 4, 5, 6]

result = {
    'pares': list(filter(lambda x: x % 2 == 0, num_list)),
    'ímpares': list(filter(lambda x: x % 2 != 0, num_list))
}

print(result)

'''
Aqui, usei filter() e lambda para separar os números pares e ímpares em um dicionário.
Foi um exercício tranquilo, foi só desenvolver a lógica e ver como funciona a relação com dicionário e se dava pra aplicá-la diretmente a estrutura do dicionário.
'''