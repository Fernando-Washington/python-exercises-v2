# 1. Dobrar elementos de uma lista (com map) 

'''
Escreva uma função que, utilizando map e uma função lambda, receba uma lista de números inteiros e retorne uma nova lista com todos os elementos dobrados. 

Exemplo de entrada: [1, 2, 3, 4] 
Exemplo de saída: [2, 4, 6, 8]
'''

num_list = [1, 2, 3, 4]

double = list(map(lambda x: x*2, num_list))

print(double)

'''
Esse exercício foi bem tranquilo. Já tinha uma noção de como o map() funciona, mas foi a primeira vez que usei fora da aula junto com uma função lambda. Achei bem interessante como a lambda permite criar uma função simples em uma linha.
No começo, fiquei um pouco confuso com a sintaxe, mas depois de alguns testes, consegui entender como ela funciona.
'''