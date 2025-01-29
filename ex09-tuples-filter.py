from functools import reduce

# 9. Filtrar tuplas com média maior que 5

'''
Escreva uma função que receba uma lista de tuplas, onde cada tupla contém
números inteiros. Utilize map e filter para filtrar as tuplas cuja média dos valores seja maior que 5.

Exemplo de entrada: [(2, 8), (4, 5, 6), (1, 2)]
Exemplo de saída: [(2, 8), (4, 5, 6)]
'''

tuples_list = [(2, 8), (4, 5, 6), (1, 2)]

result = list(filter(lambda x: sum(x) / len(x) >= 5, tuples_list))

print(result)

# por algum motivo isso não funciona com map
#result = list(map(lambda x: sum(x) / len(x), filter(lambda x: x > 5 , tuples_list)))