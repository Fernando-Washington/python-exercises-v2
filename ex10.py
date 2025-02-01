from functools import reduce
#10. Média ponderada com dicionário e reduce
'''
Crie uma função que receba um dicionário onde as chaves são nomes de alunos e os valores são listas de notas (com pesos na última posição). 
A função deve calcular a média ponderada de cada aluno usando reduce e retornar um novo dicionário com os resultados.

Exemplo de entrada:
{
 "João": [8, 7, 9, 2], # (notas: 8, 7, 9; peso: 2)
 "Ana": [5, 6, 7, 3] # (notas: 5, 6, 7; peso: 3)
}

Exemplo de saída:
{
 "João": 8.0,
 "Ana": 6.0
}
'''

dictionary = {
 "João": [8, 7, 9, 2], # (notas: 8, 7, 9; peso: 2)
 "Ana": [5, 6, 7, 3] # (notas: 5, 6, 7; peso: 3)
}

result = dict(map(
    lambda item: (
        item[0],  # Nome do aluno
        reduce(lambda acc, x: acc + x[0] * x[1], zip(item[1][:-1], [item[1][-1]] * (len(item[1]) - 1)), 0) / (item[1][-1] * (len(item[1]) - 1))
    ), dictionary.items()
))

print(result)

# media_ponderada = (notas * peso) / peso
