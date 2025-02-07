# 2. Filtrar números pares de uma lista (com filter)

'''
Escreva uma função que, utilizando filter e uma função lambda, receba uma lista de números inteiros e retorne apenas os números pares. 

Exemplo de entrada: [1, 2, 3, 4, 5] 
Exemplo de saída: [2, 4]
'''

num_list = [1, 2, 3, 4, 5] 

num_pair = list(filter(lambda x: x % 2 == 0, num_list))

print(num_pair)

'''
Aqui, usei a função filter() junto com lambda para filtrar apenas os números pares de uma lista.
Foi bem interessante ver como o filter() funciona, mas confesso que no início fiquei um pouco confuso sobre como ele retorna um iterador e precisei converter o resultado para uma lista. 
Depois que entendi, achei bem simples e útil para situações em que precisamos selecionar elementos específicos de uma lista.
'''