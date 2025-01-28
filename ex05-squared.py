# 5. Elevar números ao quadrado e ordenar (com map e sorted)

'''
Crie uma função que eleve ao quadrado todos os números de uma lista, utilizando
map, e depois retorne a lista ordenada.

Exemplo de entrada: [3, 1, 4, 2]
Exemplo de saída: [1, 4, 9, 16]
'''

num_list = [3, 1, 4, 2]

num_squared = list(map(lambda x: x**2, num_list))

sorted_num = sorted(num_squared)

print(sorted_num)

