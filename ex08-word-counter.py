from functools import reduce

# 8. Contar letras em uma lista de palavras (com map e reduce)

'''
Crie uma função que receba uma lista de palavras e retorne a soma total de letras
em todas as palavras, utilizando map para contar as letras e reduce para somar.

Exemplo de entrada: ["casa", "python", "lambda"]
Exemplo de saída: 16
'''

word_list = ["casa", "python", "lambda"]

result = reduce(lambda x, y: x + y, list(map(lambda x: len(x), word_list)))

print(result)

'''
Esse exercício foi mais complicado, tive que combinar map(), reduce() e lambda para contar o total de letras em uma lista de palavras. A maior dificuldade foi entender aonde ia o reduce(), mas depois que peguei o jeito, foi bem útil. Achei interessante como dá para usar essas funções para resolver problemas complexos de forma elegante.
'''