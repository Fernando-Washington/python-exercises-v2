# 4. Nomes com mais de 5 letras (com filter)

'''
Escreva uma função que receba uma lista de nomes e, utilizando filter, retorne apenas os nomes com mais de 5 letras.

Exemplo de entrada: ["Ana", "Lucas", "Fernanda", "João"]
Exemplo de saída: ["Lucas", "Fernanda"]
'''

name_list = ["Ana", "Lucas", "Fernanda", "João"]

name_filter = list(filter(lambda x: len(x) >= 5, name_list))

print(name_filter)

'''
Esse exercício foi bem tranquilo. Usei filter() e lambda para filtrar os nomes com mais de 5 letras.
Achei interessante como o filter() permite selecionar elementos de uma lista de forma simples e eficiente.
No começo, fiquei em dúvida se deveria usar ">" ou ">=" para incluir nomes com exatamente 5 letras,
mas decidi usar ">=" para incluir "Lucas", como no exemplo dado.
'''