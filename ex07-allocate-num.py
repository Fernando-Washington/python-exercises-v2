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

'''
Esse exercício foi uma versão mais elaborada do 6 sendo um pouco mais complexo, mas consegui resolver usando map(), filter() e lambda facilmente.
A maior dificuldade foi entender como estruturar o dicionário com as categorias, e achei melhor estruturar não colocando ele diretamente como no anterior.
Assim ficou simples e fácil de um colega de trabalho entender de primeira o que está acontecendo no código.
'''