"""
https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

Você receberá um array de números. Sua tarefa é ordenar apenas os números ímpares em ordem crescente,
mantendo os números pares em suas posições originais.
Exemplos:

[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

>>> ordena_impares([7, 1])
[1, 7]

>>> ordena_impares([5, 8, 6, 3, 4])
[3, 8, 6, 5, 4]

>>> ordena_impares([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
[1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""

def ordena_impares(lista_a_ordenar):
    lista_impares = sorted([item for item in lista_a_ordenar if item % 2])

    # for item in lista_a_ordenar:
    #     if item % 2:
    #         lista_impares.append(item)

    return [item if item % 2 == 0 else lista_impares.pop(0) for item in lista_a_ordenar]

    """for item in lista_a_ordenar:
        if item % 2 != 0:
            resultado.append(lista_impares.pop(0))
        else:
            resultado.append(item)
    """
    # return resultado