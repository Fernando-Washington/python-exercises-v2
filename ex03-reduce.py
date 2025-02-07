from functools import reduce

# 3. Somar os números de uma lista (com reduce)

'''
Crie uma função que, utilizando reduce e uma função lambda, receba uma lista de números inteiros e retorne a soma total dos números.

Exemplo de entrada: [1, 2, 3, 4]
Exemplo de saída: 10
'''

num_list = [1, 2, 3, 4]

sum_result = reduce(lambda x, y: x + y, num_list)

print(sum_result) 

# x = 1 + y = 2 = 3
# x = 3 + y = 3 = 6
# x = 6 + y = 4 = 10

'''
Esse exercício foi um pouco mais complexo do que os demais porém foi só ver a sintaxe na documentação que as coisas fluiram. 
Entendi que ela aplica a função lambda em pares de elementos até reduzir a lista a um único valor.
Depois que peguei o jeito.
'''