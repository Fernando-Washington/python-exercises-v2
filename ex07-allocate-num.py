# 7. Agrupar números em categorias (com dicionários e lambdas)

'''
Escreva uma função que receba uma lista de números inteiros e utilize map e filter
para criar um dicionário que agrupe os números em três categorias:

o "positivos" (números maiores que 0)
o "negativos" (números menores que 0)
o "zeros" (números iguais a 0).
o Exemplo de entrada: [1, -2, 0, 3, -5, 0]
o Exemplo de saída: {"positivos": [1, 3], "negativos": [-2, -5], "zeros": [0, 0]}'''

def num_organized(num_list):
  
    positives = list(map(lambda x: x, filter(lambda x: x > 0, num_list)))
    negatives = list(map(lambda x: x, filter(lambda x: x < 0, num_list)))
    zeros = list(map(lambda x: x, filter(lambda x: x == 0, num_list)))
        
    return {
        'positivos': positives,
        'negativos': negatives,
        'zeros': zeros
    }

print(num_organized([1, -2, 0, 3, -5, 0]))