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

'''
Nesse exercício, usei map() para elevar os números ao quadrado e depois sorted() para ordenar a lista.
Foi bem tranquilo, mas precisei lembrar que o map() retorna um iterador, então precisei convertê-lo para uma lista antes de usar o sorted(). Achei interessante como dá para combinar essas funções para fazer operações complexas em poucas linhas de código, acaba sendo bem mais prático do que fazer uma única função do zero para isso.
'''