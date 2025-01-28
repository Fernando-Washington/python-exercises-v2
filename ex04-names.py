# 4. Nomes com mais de 5 letras (com filter)

'''
Escreva uma função que receba uma lista de nomes e, utilizando filter, retorne apenas os nomes com mais de 5 letras.

Exemplo de entrada: ["Ana", "Lucas", "Fernanda", "João"]
Exemplo de saída: ["Lucas", "Fernanda"]
'''

name_list = ["Ana", "Lucas", "Fernanda", "João"]

name_filter = list(filter(lambda x: len(x) >= 5, name_list))

print(name_filter)

# Obs: deixei '>=' ou Lucas não estaria incluído como no seu exemplo